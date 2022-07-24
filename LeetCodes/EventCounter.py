import memcache
import datetime

class UpperCacheLevel:
	SEC = 0
	MIN = 1
	HOUR = 2
	DAY = 3
	MONTH = 4
	YEAR = 5

class EventCounter:

	def now(self, unit):
		'''

		:param unit: UpperCacheLevel
		:return:
		'''
		time_now = datetime.datetime.now()
		year, month, day = time_now.year, time_now.month, time_now.day
		hour, min, second = time_now.hour, time_now.min, time_now.second
		base = "{}-{}-{}".format(year, month, day)

		if unit <= UpperCacheLevel.HOUR:
			base = "{}-{}".format(base, hour)

		if unit <= UpperCacheLevel.MIN:
			base = "{}-{}".format(base, min)

		if unit <= UpperCacheLevel.MIN:
			base = "{}-{}".format(base, second)

		return base

	def decide_upper_level_cache(self, look_back):
		# level = UpperCacheLevel.SEC if look_back is less than 1 min,
		# level = UpperCacheLevel.MIN, if look_back is less than 1 hour
		# level = UpperCacheLevel.HOUR, if look_back is less than 1 Day
		# level = UpperCacheLevel.DAY, if look_back is longer than 1 day
		return level

	def __init__(self, look_back, host='127.0.0.1:12000'):
		'''
		Memcache would be a good choice here, to aggregate number of events within a constant recent time. For this problem,
		we don't need to store/persist all the history log (keys).

		Key would be the Time represented as YEAR-MONTH-DAY-HOUR-MIN-SEC, the value would be the sum of the corresponding count.

		Given size of look_back (constant), if it is short(only several seconds), we can have only one cache at second level.
		If it is longer like 50 minutes, we can have two levels of cache, one second cache and one minute cache. If look_back is even
		longer like days, months, we can just add more levels of cache to handle the problem.

		For second, min, hour, Day layer
		we need to set an expiration time to drop keys(time) in the past, we don't need to store all the history log cnt.
		For second layer cache: key is like 2018-JAN-01-23:42:34, and the key will be expired (deleted) after one minute
		For minute layer cache: key is like 2018-JAN-01-23:42, and the key will expired after one minute
		For hour layer cache: key is like 2018-JAN-01-23, and the key will expire after one Day
		For day layer cache: Key is like 2018-Jan-01, and the key will expire after one month.


		:param look_back: Constant N, define the duration how long we should look back to aggregate the event cnt. Here we use
		second as unit. Eg, N == 30, means recent 30 second, N == 361 means recent 60 mins and 1 second
		'''
		self.host = host
		self.look_back = look_back
		self.cache_second = memcache.Client([self.host],debug=0)

		# init upper level cache as None
		self.cache_min = self.cache_hour = self.cache_day = None
		self.upper_level = self.decide_upper_level_cache(look_back)

		if self.upper_level >= UpperCacheLevel.MIN:
			self.cache_min = memcache.Client([self.host],debug=0)

		if self.upper_level >= UpperCacheLevel.HOUR:
			self.cache_hour_cnt = memcache.Client([self.host],debug=0)

		if self.upper_level >= UpperCacheLevel.HOUR:
			self.cache_day = memcache.Client([self.host],debug=0)

	def event_occur(self):
		time_now_second = self.now("SEC")
		self.cache_second.increament(time_now_second, ttl="60s")

		if self.upper_level >= UpperCacheLevel.MIN:
			time_now_min = self.now("MIN")
			self.cache_min.increament(time_now_min, ttl="60m")

		if self.upper_level >= UpperCacheLevel.HOUR:
			time_now_hour = self.now("HOUR")
			self.cache_hour.increament(time_now_hour, ttl="1d")

		if self.upper_level >= UpperCacheLevel.DAY:
			time_now_day = self.now("DAY")
			# Since day level is already pretty high, for 100 years, we have 36,500 Days, 36.5k keys should be fine
			# to put in memory. And if we have month/YEAR level of cache, we need to update more caches each time we updating
			self.cache_hour.increament(time_now_day, ttl="INF")

	def parse_time(self, time):
		'''
		Return
		:param time: N seconds
		:return: (#YEAR, #MONTH, #DAY, #HOUR, #MIN, #SEC)
		'''
		day = hour = min = 0
		min_interval = 60
		hr_interval = 3600
		day_interval = hr_interval * 24

		# if time is longer than a day, we represent it as #days still
		if time >= day_interval:
			day, time = divmod(time, day_interval)
		if time >= hr_interval:
			hour, time = divmod(time, hr_interval)
		if time >= min_interval:
			min, time = divmod(time, min_interval)

		sec = time
		return day, hour, min, sec

	def shift_time(self, time_to_shift, amount, unit):
		'''
		Given current time, return the time after shifting amount of units back.
		Eg. Current is 2018-Jan-02-04:55:39, shift 10 seconds back return 2018-Jan-02-04:55:29
			Current is 2018-Jan-02-04:55:39, shift 40 seconds back return 2018-Jan-02-04:54:59

		:param amount:
		:param unit:
		:return:
		'''
		return "<SHIFTED_TIME>"

	def get_recent_event_count(self):

		total_cnt = 0
		num_day, num_hour, num_min, num_second = self.parse_time(self.look_back)

		# eg: 2018-01-02-04-55-39(2018, Jan, 2, 4:55:39)
		time_now = self.now(UpperCacheLevel.SEC)

		for _ in range(num_second):
			time_now = self.shift_time(time_now, 1, UpperCacheLevel.SEC)
			total_cnt += self.cache_second.get(time_now, default=0)

		# Get the min precision of current shifted time, eg: 2018-01-02-04-55
		time_now = "-".join(time_now.split("-")[:-1])
		for _ in range(num_min):
			time_now = self.shift_time(time_now, 1, UpperCacheLevel.MIN)
			total_cnt += self.cache_min.get(time_now, default=0)

		# Get the hour precision of current shifted time, eg: 2018-Jan-02-04
		time_now = "-".join(time_now.split("-")[:-1])
		for _ in range(num_hour):
			time_now = self.shift_time(time_now, 1, UpperCacheLevel.HOUR)
			total_cnt += self.cache_hour.get(time_now, default=0)

		# Get the day precision of current shifted time, eg: 2018-Jan-02
		time_now = "-".join(time_now.split("-")[:-1])
		for _ in range(num_day):
			time_now = self.shift_time(time_now, 1, UpperCacheLevel.DAY)
			total_cnt += self.cache_day.get(time_now, default=0)



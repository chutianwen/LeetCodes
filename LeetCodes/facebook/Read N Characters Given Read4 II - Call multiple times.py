'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1:

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2:

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""

'''


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution2:
	# @param buf, Destination buffer (a list of characters)
	# @param n,   Maximum number of characters to read (an integer)
	# @return     The number of characters read (an integer)
	def __init__(self):
		self.queue = []

	def read(self, buf, n):
		idx = 0
		while True:
			buf4 = [""]*4
			l = read4(buf4)
			self.queue.extend(buf4)
			curr = min(len(self.queue), n-idx)
			for i in xrange(curr):
				buf[idx] = self.queue.pop(0)
				idx+=1
			if curr == 0:
				break
		print(buf4)

		return idx + 1


from collections import deque
class Solution(object):

	def __init__(self):
		self.buffer = deque()

	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
		:rtype: The number of characters read (int)
		"""
		start = 0

		need_cache = min(n, len(self.buffer))
		buf[start: start + need_cache] = [self.buffer.popleft() for _ in range(need_cache)]
		start += need_cache
		n -= need_cache

		tmp_buff = [0] * 4
		while n > 0:
			num_real = read4(tmp_buff)
			if num_real == 0:
				break
			else:
				# if we still need to read4, then whole tmpBuff will be used.
				if n >= num_real:
					buf[start: start + num_real] = tmp_buff
					start += num_real
				else:
					# if we read 3 chars but only need 2, then tmp_buff[n: num_real] should be push to global queue.
					buf[start: start + n] = tmp_buff[:n]
					self.buffer.extend(tmp_buff[n:num_real])
					start += n

				n -= num_real

		return start
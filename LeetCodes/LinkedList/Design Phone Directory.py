'''
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);

'''

class PhoneDirectory(object):

	def __init__(self, maxNumbers):
		self.directory = [i for i in range(maxNumbers)]


	def get(self):
		if len(self.directory)==0:
			return -1
		return self.directory.pop(0)

	def check(self, number):
		return number in self.directory


	def release(self, number):
		if number not in self.directory:
			self.directory.append(number)

		# Your PhoneDirectory object will be instantiated and called as such:
		# obj = PhoneDirectory(maxNumbers)
		# param_1 = obj.get()
		# param_2 = obj.check(number)
		# obj.release(number)
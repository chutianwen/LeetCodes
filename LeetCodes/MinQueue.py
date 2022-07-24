from collections import deque
class MinQueue(deque):
	def __init__(self):
		super().__init__()
		self.mins = deque()

	def append(self, x):
		super().append(x)
		while self.mins and x < self.mins[-1]:
			self.mins.pop()
		self.mins.append(x)

	def popleft(self):
		x = super().popleft()
		if self.mins[0] == x:
			self.mins.popleft()
		return x

	def min(self):
		return self.mins[0]

class MaxQueue(deque):

	def __init__(self):
		deque.__init__(self)
		self.max = deque()

	def append(self, x):
		deque.append(x)
		while self.max and self.max[-1] < x:
			self.max.pop()
		self.max.append(x)

	def popleft(self):
		x = deque.popleft(self)
		if x == self.max[0]:
			self.max.popleft()
		return x

	def max(self):
		return self.max[0]


q = MinQueue()
q.append(4)
q.append(3)
q.append(5)
print(q.popleft())
print(q.min())


a = [1]
def fun():
	a[0] += 2
fun()
print(a)
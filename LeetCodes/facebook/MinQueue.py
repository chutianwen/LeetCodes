from collections import deque

class MinQueue(deque):

	def __init__(self):
		deque.__init__(self)
		self.mins = deque()

	def append(self, x):
		deque.append(self, x)
		while self.mins and x < self.mins[-1]:
			self.mins.pop()
		self.mins.append(x)

	def popleft(self):
		x = deque.popleft(self)
		if self.mins[0] == x:
			self.mins.popleft()
		return x

	def min(self):
		return self.mins[0]


q = MinQueue()
i = [2,4,1,2,5,3]
for x in i:
	q.append(x)
help()
print(q)
print(q.mins)
while q:
	print(q.min(), q.popleft())
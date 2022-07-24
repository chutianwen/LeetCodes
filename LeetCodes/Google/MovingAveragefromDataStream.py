'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) == self.size:
            self.window.popleft()
        self.window.append(val)
        return sum(self.window)/len(self.window)

class MovingAverage2(object):
    '''
    Using circular array, no need to re-calculate sum each time.
    idx is always increasing when calling next, but using idx % size to decide which element of index should be updated.
    '''
    def __init__(self, size):
        self.vect, self.sums, self.idx, self.size = [0] * size, 0, 0, size


    def next(self, val):
        self.idx += 1
        self.sums -= self.vect[self.idx % self.size]
        self.vect[self.idx % self.size] = val
        self.sums += val
        return self.sums / float(min(self.idx, self.size))


        # Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
param_1 = obj.next(10)
print(param_1)
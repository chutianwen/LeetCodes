'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class CacheNode:

	def __init__(self, k, v):
		self.k = k
		self.v = v
		self.next = None
		self.pre = None


class LRUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity
		self.map = dict()
		self.head = CacheNode(0, 0)
		self.tail = CacheNode(0, 0)
		self.head.next = self.tail
		self.tail.pre = self.head

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		if key not in self.map:
			return -1
		else:
			node = self.map[key]
			self.remove(node)
			self.add(node)
			return node.v

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: void
		"""
		if key in self.map:
			node = self.map[key]
			self.remove(node)
		elif len(self.map) == self.capacity:
			self.map.pop(self.tail.pre.k, None)
			self.remove(self.tail.pre)

		node = CacheNode(key, value)
		self.map[key] = node
		self.add(node)

	def remove(self, node):
		pre = node.pre
		next = node.next
		pre.next = next
		next.pre = pre


	def add(self, node):
		ori = self.head.next
		self.head.next = node
		node.pre = self.head
		node.next = ori
		ori.pre = node

		# Your LRUCache object will be instantiated and called as such:
		# obj = LRUCache(capacity)
		# param_1 = obj.get(key)
		# obj.put(key,value)

cache = LRUCache(1)
cache.put(2, 1)
print(cache.get(2))
cache.put(3, 2)
print(cache.get(2))
print(cache.get(3))

'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

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



class LRUCache(object):

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.pre = None

    def __init__(self, capacity):
        """
        Using dict to store key=key, value=reference to node
        Using double linkedlist to update node or delete node.
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cnt = 0

    def update(self, node):
        self.remove(node)
        self.add(node)

    def remove(self, node):
        # node.next.pre = node.pre
        # node.pre.next = node.next
        node.next.pre, node.pre.next = node.pre, node.next

    def add(self, node):
        '''
        Be careful that cannot use the oneline code here.
        :param node:
        :return:
        '''
        after = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = after
        after.pre = node
        # self.head.next, self.head.next.pre, node.next, node.pre = node, node, self.head.next, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            self.update(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.map:
            node = self.Node(key, value)
            self.add(node)
            if self.cnt >= self.capacity:
                node_remove = self.tail.pre
                self.map.pop(node_remove.key)
                self.remove(node_remove)
                self.cnt -= 1
            self.map[key] = node
            self.cnt += 1
        else:
            node = self.map[key]
            node.value = value
            self.update(node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
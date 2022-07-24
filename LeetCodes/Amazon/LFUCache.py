'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following
operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''
class LFUCache(object):

    class Node:
        def __init__(self, key, value, size=0):
            self.key = key
            self.value = value
            self.size = size
            self.pre = None
            self.next = None

    class mylist:
        def __init__(self):
            self.head = LFUCache.Node(0, 0)
            self.tail = LFUCache.Node(0, 0)
            self.head.next, self.tail.pre = self.tail, self.head

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.multi_list = {}
        self.capacity = capacity

    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        if self.multi_list[node.size].head.next == self.multi_list[node.size].tail:
            self.multi_list.pop(node.size)

    def add(self, node):
        if node.size not in self.multi_list:
            self.multi_list[node.size] = self.mylist()

        after = self.multi_list[node.size].head.next
        self.multi_list[node.size].head.next = node
        node.pre = self.multi_list[node.size].head
        node.next = after
        after.pre = node

    def update(self, node):
        self.remove(node)
        node.size += 1
        self.add(node)

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
        # this is very important!
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.update(node)
        else:
            node = self.Node(key, value, 1)
            if len(self.map) >= self.capacity:
                min_size = min(self.multi_list.keys())
                node_remove = self.multi_list[min_size].tail.pre
                self.remove(node_remove)
                self.map.pop(node_remove.key)
            self.add(node)
            self.map[key] = node


from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count

from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1


class LFUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyToNode = dict()
        self.countToKeyNode = defaultdict(OrderedDict)
        self.min_cnt = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        self.countToKeyNode[node.cnt].pop(key)
        if not self.countToKeyNode[node.cnt]:
            self.countToKeyNode.pop(node.cnt)
            if self.min_cnt == node.cnt:
                self.min_cnt += 1

        node.cnt += 1
        self.countToKeyNode[node.cnt][key] = node

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.capacity:
            return

        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.value = value
            self.get(key)
        else:
            if len(self.keyToNode) == self.capacity:
                old_key, _  = self.countToKeyNode[self.min_cnt].popitem(last=False)
                self.keyToNode.pop(old_key)

            new_node = Node(key, value)
            self.keyToNode[key] = new_node
            self.countToKeyNode[1][key] = new_node
            self.min_cnt = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
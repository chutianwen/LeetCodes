"""
A linked list is given such that each node contains an additional random pointer which could point to any node in
the list or null.

Return a deep copy of the list.
"""
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        The trick is to link the random node.
        Using a map to store: original object -> new object.
        Considering map[p] as a reference.
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        map = {}
        p = head
        while p:
            map[p] = RandomListNode(p.label)
            p = p.next
        p = head
        while p:
            map[p].next = map.get(p.next, None)
            map[p].random = map.get(p.random, None)
            p = p.next
        return map[head]
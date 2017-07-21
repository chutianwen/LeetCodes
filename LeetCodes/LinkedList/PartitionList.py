"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

from ListNode import ListNode
class Solution(object):
    def partition(self, head, x):
        """
        Two pointers, one pointing to a list smaller than target, one pointing to list larger or equal than target
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        lo_head = lo = ListNode(0)
        hi_head = hi = ListNode(0)
        p = head
        while p:
            if p.val < x:
                lo.next = p
                lo = lo.next
            else:
                hi.next = p
                hi = hi.next
            p = p.next
        hi.next = None
        lo.next = hi_head.next
        return lo_head.next

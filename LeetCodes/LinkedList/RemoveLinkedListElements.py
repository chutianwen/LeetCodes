"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""

from ListNode import ListNode
class Solution(object):
    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            p1 = head
            while p1 and p1.next:
                if p1.next.val == val:
                    p1.next = p1.next.next
                else:
                    p1 = p1.next
            if head.val == val:
                return head.next

        return None

    def removeElements(self, head, val):

        if head is None:
            return None
        else:
            head.next = self.removeElements(head.next, val)
            return head if head.val != val else head.next
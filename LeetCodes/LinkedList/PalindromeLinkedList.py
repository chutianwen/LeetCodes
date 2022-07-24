"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
from ListNode import ListNode

class Solution(object):
    def isPalindrome(self, head):
        """
        use fast and slow pointer to reach the mid
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        else:
            p1 = p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            p1 = p1.next

            rev = None
            while p1:
                rev, rev.next, p1 = p1, rev, p1.next

            while p1:
                if p1.val != rev.val:
                    return False
                head = head.next
                rev = rev.next
            return True
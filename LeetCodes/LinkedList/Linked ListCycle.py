"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


from ListNode import ListNode
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        else:
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
                if p1 == p2:
                    return True
            return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow = fast = head
        is_first = True
        while fast and fast.next:
            if not is_first and slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
            is_first = False
        return False
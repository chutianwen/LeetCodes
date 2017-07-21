"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.


"""
from ListNode import ListNode
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        cnt = 0
        tail = head
        # get the length and tail
        while tail:
            cnt += 1
            if tail.next:
                tail = tail.next
            else:
                break
        k = cnt - k % cnt
        # needs to consider the case no rotate needed, if so, return the original list.
        if k == cnt:
            return head
        head_new = head
        for i in range(k):
            tmp = head_new.next
            # chop the tail at the end
            if i == k - 1:
                head_new.next = None
            head_new = tmp
        tail.next = head
        return head_new
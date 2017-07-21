"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

from ListNode import ListNode
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Trick is going through list combined from both. Seek two paths having same length
        L1 + L2 - Intersection == L2 + L1 - Intersection.
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        p1 = headA
        p2 = headB

        # when p1 and p2 reaches end, they will both become None, then loop ends even without intersection.
        while p1 != p2:
            # !!! has to use if p1 not if p1.next, otherwise it will not end loop when there is no intersection.
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

head3 = ListNode(1)
head1 = ListNode(9)
head2 = ListNode(4)
head1.next = head3
head2.next = ListNode(5)
# head2.next.next = head3


res = Solution().getIntersectionNode(head1, head2)
print(res.val)
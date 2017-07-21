"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.


"""
from ListNode import ListNode
class Solution(object):
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = cur = ListNode(0)
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return head.next

    def mergeTwoLists(self, l1, l2):

        if not l1 or not l2:
            return l1 or l2
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    def mergeTwoLists3(self, l1, l2):
        """
        merge in place, needs more thoughts

        :param l1:
        :param l2:
        :return:
        """
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

def fun(l1, l2):
    if not l1 or not l2:
        return l1 or l2

res = fun(None, None)
print(res.val)

# a = b = ListNode(1)
# a.next = ListNode(2)
# print(b.next.val)
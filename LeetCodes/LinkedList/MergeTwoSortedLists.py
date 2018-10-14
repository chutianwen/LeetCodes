"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.


"""
from ListNode import ListNode
class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        cur = dummy = ListNode(0)
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1 or p2:
            cur.next = p1 or p2
        return dummy.next


    def mergeTwoLists2(self, l1, l2):

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
        merge in place, pointer 'nxt' will always pointing next node in l1.
        After loop, just check if l2 has left or not. If has, then cat l2 to the cur.next
        l1: 1 -> 3 -> 5
        l2: 2 -> 4 -> 6
        step1 : dummy -> 1 -> 2 -> 3 -> 5
        step2 : dummy -> 1 -> 2 -> 3 -> 4 -> 5
        step3 : dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

        l1: 4 -> 5 -> 6
        l2: 1 -> 2 -> 3
        step1: dummy -> 1 -> 4 -> 5 -> 6
        step2: dummy -> 1 -> 2 -> 4 -> 5 -> 6
        step3: dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
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
        if l2 is not None:
            cur.next = l2
        return dummy.next

def fun(l1, l2):
    if not l1 or not l2:
        return l1 or l2

res = fun(None, None)
print(res.val)

# a = b = ListNode(1)
# a.next = ListNode(2)
# print(b.next.val)
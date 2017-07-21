"""
Reverse a singly linked list.
"""
from ListNode import ListNode

class Solution(object):
    def reverseList2(self, head):
        """
        modify in place
        :type head: ListNode
        :rtype: ListNode
        """
        # p1 is the old head
        if head is None:
            return None
        p1 = head
        p2 = head.next
        while p2:
            tmp = p2.next
            p2.next = head
            head = p2
            p1.next = tmp
            p2 = tmp
        return head

    def reverseList3(self, head):
        """
        using another list, original list pop() and current list inserted
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        p = head
        rev = None
        while p:
            temp2 = rev
            temp3 = p.next
            rev = p
            rev.next = temp2
            p = temp3
            # rev, rev.next, p = p, rev, p.next
        return rev

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            # actually head.next.next is the tail on the new reversed list, so tail.next = head
            head.next.next = head
            head.next = None
            return new_head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
res = Solution().reverseList3(head)
p = res

while p:
    print(p.val)
    p = p.next

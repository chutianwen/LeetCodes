"""
Reverse a singly linked list.
"""
from ListNode import ListNode

class Solution(object):
    def reverseList1(self, head):
        """
        modify list in place, needs three pointers.
        1). Old head, which will become the tail at the end. old head.next should be the future head node
        2). Next node: The one gonna become the new head, then back pointing to the next one in original list.
        3). New Head: The new head of reversed list.
        :type head: ListNode head will always pointing to the head of new reversed list.
        :rtype: ListNode
        """
        if head is None:
            return None
        head_old = head
        new_node = head.next
        while new_node:
            tmp = new_node.next
            new_node.next = head
            head = new_node
            new_node = tmp
        # cut the tail
        head_old.next = None
        return head

    def reverseList2(self, head):
        """
        Creating another head, and grow this new list while chopping the original list.
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        p = head
        # new List
        rev = None
        while p:
            temp3 = p.next
            p.next = rev
            rev = p
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
            # actually head.next is the tail on the new reversed list, so tail.next = head
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

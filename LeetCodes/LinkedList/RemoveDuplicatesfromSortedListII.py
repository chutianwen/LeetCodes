"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


"""
from ListNode import ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        Needs clear mind about checking current one and next one.
        preone and cur one won't work in this case.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        else:
            p = fake_head = ListNode(0)
            pre = None
            cur = head
            while cur:
                if pre and cur.val == pre.val:
                    cur = cur.next
                else:
                    if cur.next and cur.val != cur.next.val:
                        fake_head.next = cur
                        fake_head = fake_head.next
                    if cur.next is None and cur.val != pre.val:
                        fake_head.next = cur
                        fake_head = fake_head.next
                    pre = cur
                    cur = cur.next
            fake_head.next = None
            return p.next

root = ListNode(1)
root.next = ListNode(1)
# root.next.next = ListNode(2)
res = Solution().deleteDuplicates(root)
while res:
    print(res.val)
    res = res.next
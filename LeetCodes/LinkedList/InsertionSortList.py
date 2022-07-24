"""
Sort a linked list using insertion sort.


"""
from ListNode import ListNode
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            sorted_head = self.insertionSortList(head.next)
            p1 = ListNode(0)
            p1.next = sorted_head
            if sorted_head.val > head.val:
                head.next = sorted_head
                sorted_head = head
                return sorted_head
            else:
                # <= is tricky thing here.
                while p1.next and p1.next.val <= head.val:
                    p1 = p1.next
                if p1.next is None:
                    p1.next = head
                    head.next = None
                else:
                    tmp = p1.next
                    p1.next = head
                    head.next = tmp
                return sorted_head

root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
res = Solution().insertionSortList(root)
while res:
    print(res.val)
    res = res.next
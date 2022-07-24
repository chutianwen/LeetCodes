"""
Sort a linked list in O(n log n) time using constant space complexity.


"""
from ListNode import ListNode
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def mergesort(head):

            if head is None or head.next is None:
                return head
            else:
                p1 = p2 = head
                while p2.next and p2.next.next:
                    p1 = p1.next
                    p2 = p2.next.next
                tmp = p1.next
                p1.next = None
                p1 = tmp

                left = mergesort(head)
                right = mergesort(p1)
                return merge(left, right)

        def merge(l1, l2):
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

        res = mergesort(head)
        return res


root = ListNode(1)
res = Solution().sortList(root)
print(res)
while res:
    print(res.val)
    res = res.next
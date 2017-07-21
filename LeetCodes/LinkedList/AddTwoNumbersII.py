"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from ListNode import ListNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = ""
        str2 = ""
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        num1 = int(str1)
        num2 = int(str2)
        res = str(num1 + num2)
        p = head = ListNode(0)
        for n in res:
            p.next = ListNode(n)
            p = p.next
        return head.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)

l2= ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(1)
res = Solution().addTwoNumbers(l1, l2)

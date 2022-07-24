'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		p1, p2 = l1, l2
		carry = 0

		if not p1 and p2:
			return p2

		while p1 or p2 or carry:
			v = 0
			if p1 and p2:
				v = p1.val + p2.val
			elif p1 and not p2:
				if carry == 0:
					break
				v = p1.val

			v += carry
			carry, p1.val = divmod(v, 10)

			if p1.next is None:
				if p2 and p2.next:
					p1.next = p2.next
					p1 = p1.next
					p2 = None
				else:
					if carry != 0:
						p1.next = ListNode(carry)
					break
			else:
				p1 = p1.next
				if p2:
					p2 = p2.next

		return l1
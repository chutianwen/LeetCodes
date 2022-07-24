'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


'''


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):


	def reverseListIterative(self, head):

		new_head = None
		while head:

			# watch out, this order is not right!!!
			# in this case, head will be head.next first, so head can be None, then head.next = new_head will have problem.
			# new_head, head, head.next = head, head.next, new_head

			head.next, new_head, head = new_head, head, head.next
		return new_head

	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next: return head
		else:
			node = self.reverseList(head.next)
			head.next.next= = head
			head.next = None
			return node
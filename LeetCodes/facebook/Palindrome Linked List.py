'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head: return True
		slow = fast = head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		new_head = None

		while slow:
			tmp = slow.next
			slow.next = new_head
			new_head = slow
			slow = tmp

		while new_head:
			if head.val != new_head.val:
				return False
			head = head.next
			new_head = new_head.next
		return True


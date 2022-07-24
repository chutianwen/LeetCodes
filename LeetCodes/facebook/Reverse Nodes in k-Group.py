'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def reverseKGroupDummyHead(self, head, k):
		dummy = last = ListNode(0)
		cur = head
		while cur:
			first, cnt = cur, 1
			while cnt < k and cur:
				cur, cnt = cur.next, cnt + 1
			if cnt == k and cur:
				cur, prev = first, None
				for _ in range(k):
					prev, cur.next, cur = cur, prev, cur.next
				last.next, last = prev, first
			else:
				last.next = first
		return dummy.next


	def reverseKGroup(self, head, k):
		cur = head
		result = None
		while cur:
			first, cnt = cur, 1
			while cnt < k and cur:
				cnt += 1
				cur = cur.next

			if cnt == k and cur:
				cur = first
				pre = None
				for _ in range(k):
					cur.next, pre, cur = pre, cur, cur.next

				if not result:
					result = pre
					last = first
				else:
					last.next, last = pre, first
			else:
				if not result or not last:
					result = first
				else:
					last.next = first

		return result

	def print_list(self, head):

		while head:
			print(head.val)
			head = head.next

	def print_length(self, head):

		if not head:
			return 0
		cnt = 1
		while head:
			cnt += 1
			head = head.next
		print(cnt - 1)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Solution().print_list(head)
print("\n")
res = Solution().reverseKGroup(head, 2)
Solution().print_length(res)


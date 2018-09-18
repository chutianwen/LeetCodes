'''
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
Seen this question in a real interview before?

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def plusOne(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return ListNode(1)

		# reverse list
		new_head = None
		while head:
			head.next, new_head, head = new_head, head, head.next

		cur = new_head
		cur.val += 1
		carry = 0
		while carry or cur:

			cur.val += carry
			if cur.val == 10:
				cur.val -= 10
				carry = 1
				if not cur.next:
					cur.next = ListNode(1)
					break
				cur = cur.next
			else:
				break

		cur = new_head
		new_head = None

		while cur:
			cur.next, new_head, cur = new_head, cur, cur.next

		return new_head



input = range(1, 5)
head = dummy = ListNode(-1)

for v in input:
	dummy.next = ListNode(v)
	dummy = dummy.next

res = Solution().plusOne(head.next)

r = []
while res:
	r.append(res.val)
	res = res.next
print(r)
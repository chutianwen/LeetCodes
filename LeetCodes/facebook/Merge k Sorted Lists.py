'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) > 1:
			mid = len(lists) // 2
			left = self.mergeKLists(lists[:mid])
			right = self.mergeKLists(lists[mid:])
			res = self.merge_two_list(left, right)
			return res
		elif len(lists) == 1:
			return lists[0]
		else:
			return None

	def merge_two_list(self, list1, list2):

		dummy_head = ListNode(0)
		cur, p1, p2 = dummy_head, list1, list2
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

		return dummy_head.next

def print_list(head):
	res = []
	while head:
		res.append(head.val)
		head = head.next
	print(res)

cur_1 = l1 = ListNode(0)
for i in range(1, 5):
	cur_1.next = ListNode(i)
	cur_1 = cur_1.next

cur_2 = l2 = ListNode(5)
for i in range(6, 9):
	cur_2.next = ListNode(i)
	cur_2 = cur_2.next

print_list(l1)

print_list(l2)

a = [l1, l2]
print_list(a[0])
b = a[0]
b.next = ListNode(4)
print_list(a[0])
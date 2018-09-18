from ListNode import ListNode

class ListProblemSummary:
	'''
	Notes about list related questions

	'''
	def print_list(self, head: ListNode):
		res = []
		while head:
			res.append(head.val)
			head = head.next
		print("List: ", res)

	def iterate(self, head: ListNode):
		'''
		Notice that, after iterating, head will point to the next entry
		:param head:
		:return:
		'''

		head_copy = head
		res = []
		while head:
			res.append(head.val)
			head = head.next

		## If input is 1-2-3-4-5, and k = 2, then head_copy will point to 4
		res1 = []
		k = 3
		for _ in range(k):
			res1.append(head_copy)
			head_copy = head_copy.next

		print("Notice the val of current head_copy", head_copy.val)


	def get_mid_entry(self, head: ListNode):
		'''
		Usually this helps for solving problems of detecting palindrom. Reverse half and compare with the other half.
		This also works on divide-conquer problem by splitting original input to two parts.
		:param head:
		:return:
		'''
		slow = fast = head

		## If Input is 1-2-3-4, then slow point to 3, if Intput is 1-2-3-4-5, slow pointing to 3
		## Slow will always point to the mid or right-mid.
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		self.print_list(slow)

	def reverse_list(self, head: ListNode):
		'''
		Notice that finally first will become the last entry and first.next == None.
		new_head can also name as 'prev'
		:param head:
		:return:
		'''
		first = head
		new_head = None
		while head:
			## NOTE that
			# head.next cannot be put as second or third variable here, cuz head will be re-pointing first, and head can be None, None.next will
			# throw error.
			head.next, new_head, head = new_head, head, head.next


	def reverse_first_k(self, head: ListNode, k):

		first = head
		# can also be called new_head
		pre = None
		while head and k > 0:
			head.next, pre, head = pre, head, head.next
			k -= 1

		# before, first.next is None. Remember head already points to the next entry
		first.next = head
		self.print_list(pre)

	def reverse_k_group(self, head: ListNode, k):

		# dummy head can be a good trick of initiating result list
		dummy = last = ListNode(-1)

		cur = head
		while cur:
			# cnt should be 1, we started from first element, so it is already counted.
			first, cnt = cur, 1
			while cnt < k and cur:
				cnt += 1
				cur = cur.next

			# Need to consider if cur is None.
			if cnt == k and cur:
				# reverse from first, iterate k times
				pre = None
				head = first
				for _ in range(k):
					head.next, pre, head = pre, head, head.next

				# head is pointing to cur.next now
				cur = head
				last.next, last = pre, first
			else:
				last.next = first

		self.print_list(dummy.next)




input = range(5)
head = dummy = ListNode(-1)

for v in input:
	dummy.next = ListNode(v)
	dummy = dummy.next

tool = ListProblemSummary()

# Print list
tool.print_list(head.next)

# Get mid
tool.get_mid_entry(head.next)

# reverse k
# tool.reverse_first_k(head.next, 3)

# reverse k group
tool.reverse_k_group(head.next, 2)
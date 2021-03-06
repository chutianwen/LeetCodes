'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

'''

import collections


class Solution2(object):
	def accountsMergeCC(self, accounts):
		"""

		Connected Component and DFS traversal.
		Each CC is a user's emails
		:type accounts: List[List[str]]
		:rtype: List[List[str]]
		"""

		graph = collections.defaultdict(set)
		email_name = collections.defaultdict(str)

		for account in accounts:
			name = account[0]
			for email in account[1:]:
				graph[account[1]].add(email)
				graph[email].add(account[1])
				email_name[email] = name

		res = []

		explored = set()
		for email in graph:

			if email in explored:
				continue
			else:
				explored.add(email)
				user_emails = []
				name = email_name[email]
				frontier = [email]
				while frontier:
					expand = frontier.pop()

					user_emails.append(expand)

					for neighbor in graph[expand]:
						if neighbor not in explored:
							explored.add(neighbor)
							frontier.append(neighbor)

				res.append([name] + sorted(user_emails))

		return res

import collections

class Solution(object):
	class EmailNode:
		def __init__(self, name, email):
			self.name = name
			self.email = email
			self.parent = self
			self.rank = 0

	def findSet(self, n1: EmailNode):
		if n1 == n1.parent:
			return n1

		n1.parent = self.findSet(n1.parent)
		return n1.parent

	def union(self, n1, n2):

		p1 = self.findSet(n1)
		p2 = self.findSet(n2)

		if p1.email == p2.email:
			return

		if p1.rank >= p2.rank:
			if p1.rank == p2.rank:
				p1.rank += 1
			p2.parent = p1
		else:
			p1.parent = p2

	def accountsMerge(self, accounts):

		# email -> nodes
		email_nodes = collections.defaultdict(self.EmailNode)

		for account in accounts:
			name = account[0]

			start_node = None
			for email in account[1:]:
				if email not in email_nodes:
					email_nodes[email] = self.EmailNode(name, email)

				email_node = email_nodes[email]

				if start_node is None:
					start_node = email_node
				else:
					self.union(start_node, email_node)

		group_emails = collections.defaultdict(list)
		for email_node in email_nodes.values():
			email_group = self.findSet(email_node)
			group_emails[email_group].append(email_node.email)

		return [[group.name] + sorted(emails) for group, emails in group_emails.items()]


acc = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
res = Solution().accountsMerge(acc)
print(res)
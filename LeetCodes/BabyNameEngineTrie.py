# Your previous Plain Text content is preserved below:
#
# Build a baby names search engine.
#
# We collected baby names from various published lists and put them into a JSON object as follows:
#
# key: source list name (e.g. "2015-us-official-boys", "2015-baby-center-girls")
# value: a list of names in the order of popularity (e.g. [ "Sophia", "Emma", "Olivia", ... ])
# baby-names-data.json
#
# {
#   "2016-baby-center-girls": [ "Sophia", "Emma", "Olivia", ... ],
#   "2016-baby-center-boys": [ "Jackson", "Aiden", "Lucas", ...],
#   "2015-baby-center-girls": [ "Sophia", "Emma", "Olivia", ... ],
#   ...
# }
# The question has two parts:
#
# Write a function that given a name, returns an ascending rank sorted list of names of all lists where the given name appears.
#
# For example, given "sophia", function returns:
#
#  [
#    {list: "2016-baby-center-girls", rank: 1},
#    {list: "2015-baby-center-girls", rank: 1},
#    {list: "2015-us-official-girls", rank: 3}
#  ]
# Now, we would like to make our service more user friendly. We would like to provide a name prefix (e.g. "an") and get all baby names that start with that prefix (e.g. "anna", "anthony", etc.) along with the list name and relative ranking for each matching name.
#
# For example, given "an", function returns something like this:
#
# {
#   anna: [
#     { list: '2015-baby-center-girls', rank: 36 },
#     { list: '2016-baby-center-girls', rank: 46 }
#   ],
#   andrew: [
#     { list: '2015-baby-center-boys', rank: 44 },
#     { list: '2016-baby-center-boys', rank: 47 }
#   ],
#   anthony: [
#     { list: '2015-baby-center-boys', rank: 48 }
#   ]
# }

from collections import defaultdict
from collections import deque

class BabyNameEngineTrie:

	def __init__(self):
		self.source_rank = []
		self.children = [None] * 26

	def build(self, input):
		for source, baby_names in input.items():
			for idx, name in enumerate(baby_names, 1):
				self.add(name, (source, idx))

	def add(self, baby_name, source_rank):

		root = self
		for letter in baby_name.lower():
			idx_child = ord(letter) - ord('a')
			if root.children[idx_child] is None:
				root.children[idx_child] = BabyNameEngineTrie()
			root = root.children[idx_child]

		root.source_rank.append(source_rank)

	def search_baby(self, baby_name):
		root = self
		for letter in baby_name.lower():
			idx_child = ord(letter) - ord('a')
			if root.children[idx_child] is None:
				raise Exception("No such baby name found")
			else:
				root = root.children[idx_child]

		return root.source_rank

	def search_prefix(self, prefix):
		res = []
		root = self

		# to
		for letter in prefix:
			idx_child = ord(letter) - ord('a')
			if root.children[idx_child] is None:
				raise Exception("No such baby name found")
			else:
				root = root.children[idx_child]

		# BFS
		frontier = deque([(root, prefix)])
		while frontier:
			expand, name = frontier.popleft()

			if expand.source_rank:
				print(name, expand.source_rank)
				res.append({name: expand.source_rank})

			for idx, kid in enumerate(expand.children):
				if kid is not None:
					frontier.append((kid, name + chr(ord('a') + idx)))

		return res

class BabyNameSerachEngine:


	def __init__(self, input):
		self.baby_name_storage = defaultdict(list)

		for source, baby_names in input.items():
			for idx, name in enumerate(baby_names, 1):
				self.baby_name_storage[name].append((source, idx))

	def search_baby(self, baby_name):
		source_ranks = self.baby_name_storage[baby_name]
		source_ranks.sort(key=lambda x: x[1])
		res = defaultdict(list)
		for source, rank in source_ranks:
			res[baby_name].append({'list': source, 'rank': rank})
		return res

	def search_baby_prefix(self, baby_prefix):
		res = defaultdict(list)


input = {
	"2016-baby-center-girls": [ "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Riley", "Aria", "Zoe", "Charlotte", "Lily", "Layla", "Amelia", "Emily", "Madelyn", "Aubrey", "Adalyn", "Madison", "Chloe", "Harper", "Abigail", "Aaliyah", "Avery", "Evelyn", "Kaylee", "Ella", "Ellie", "Scarlett", "Arianna", "Hailey", "Nora", "Addison", "Brooklyn", "Hannah", "Mila", "Leah", "Elizabeth", "Sarah", "Eliana", "Mackenzie", "Peyton", "Maria", "Grace", "Adeline", "Elena", "Anna", "Victoria", "Camilla", "Lillian", "Natalie" ],
	"2016-baby-center-boys": [ "Jackson", "Aiden", "Lucas", "Liam", "Noah", "Ethan", "Mason", "Caden", "Oliver", "Elijah", "Grayson", "Jacob", "Michael", "Benjamin", "Carter", "James", "Jayden", "Logan", "Alexander", "Caleb", "Ryan", "Luke", "Daniel", "Jack", "William", "Owen", "Gabriel", "Matthew", "Connor", "Jayce", "Isaac", "Sebastian", "Henry", "Muhammad", "Cameron", "Wyatt", "Dylan", "Nathan", "Nicholas", "Julian", "Eli", "Levi", "Isaiah", "Landon", "David", "Christian", "Andrew", "Brayden", "John", "Lincoln" ],
	"2015-baby-center-girls": [ "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Zoe", "Lily", "Emily", "Madison", "Amelia", "Riley", "Madelyn", "Charlotte", "Chloe", "Aubrey", "Aria", "Layla", "Avery", "Abigail", "Harper", "Kaylee", "Aaliyah", "Evelyn", "Adalyn", "Ella", "Arianna", "Hailey", "Ellie", "Nora", "Hannah", "Addison", "Mackenzie", "Brooklyn", "Scarlett", "Anna", "Mila", "Audrey", "Isabelle", "Elizabeth", "Leah", "Sarah", "Lillian", "Grace", "Natalie", "Kylie", "Lucy", "Makayla", "Maya", "Kaitlyn" ],
	"2015-baby-center-boys": [ "Jackson", "Aiden", "Liam", "Lucas", "Noah", "Mason", "Ethan", "Caden", "Logan", "Jacob", "Jayden", "Oliver", "Elijah", "Alexander", "Michael", "Carter", "James", "Caleb", "Benjamin", "Jack", "Luke", "Grayson", "William", "Ryan", "Connor", "Daniel", "Gabriel", "Owen", "Henry", "Matthew", "Isaac", "Wyatt", "Jayce", "Cameron", "Landon", "Nicholas", "Dylan", "Nathan", "Muhammad", "Sebastian", "Eli", "David", "Brayden", "Andrew", "Joshua", "Samuel", "Hunter", "Anthony", "Julian", "Dominic" ],
	"2015-us-official-girls": [ "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte", "Harper" ],
	"2015-us-official-boys": [ "Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James", "Alexander", "Michael", "Benjamin" ]
}

# babyNameSerachEngine = BabyNameSerachEngine(input)
# res = babyNameSerachEngine.search_baby("Sophia")
# print(res)

babyNameEngineTrie = BabyNameEngineTrie()
babyNameEngineTrie.build(input)
res = babyNameEngineTrie.search_baby("Sophia")

res_prefix = babyNameEngineTrie.search_prefix("an")
print("Print out all baby with prefix")
print(res_prefix)
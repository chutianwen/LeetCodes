from fun.B import b

print("In A")
a = 5

print("In A from B", b)


class Node:
	def __init__(self, val):
		self.val = val
		self.p = None


def fun():
	input = [1,2,3]
	node = Node(input[0])
	for id in input[1:]:
		new_node = Node(id)
		new_node.p = node
		node = new_node

	return node

root = fun()
while root:
	print(root.val)
	root = root.p
print("Done")
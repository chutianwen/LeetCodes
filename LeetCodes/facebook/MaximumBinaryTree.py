'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums or len(nums) == 0: return None

		max_node = TreeNode(nums[0])
		frontier = [max_node]

		for num in nums[1:]:
			if num < frontier[-1].val:
				frontier.append(TreeNode(num))
			else:
				cur = pre_node = None

				while frontier and frontier[-1].val < num:
					cur = frontier.pop()
					if pre_node is not None:
						cur.right = pre_node

					pre_node = cur

				new_node = TreeNode(num)
				new_node.left = cur

				if len(frontier) == 0:
					max_node = new_node

				frontier.append(new_node)

		head = max_node
		for node in frontier[1:]:
			head.right = node
			head = node

		return max_node

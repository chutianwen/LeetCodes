"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both
considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child
order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""

from TreeNode import TreeNode
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
            length of sequence which is increasing, length of sequence which is decreasing
        """
        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l[0] = max(l[0], li + rd + 1, ld + ri + 1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        l = [0]
        r = dfs(root, root)
        print(r)
        return l[0]

root = TreeNode(1)
root.left = TreeNode(2)
res = Solution().longestConsecutive(root)
print(res)
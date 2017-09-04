"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child
connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def longestConsecutive(self, root):
        """
        O(n) Using global variable
        :type root: TreeNode
        :rtype: int
        """
        max_length = [0]

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left != 0 and root.val + 1 != root.left.val:
                left = 0
            if right != 0 and root.val + 1 != root.right.val:
                right = 0
            res = max(left, right) + 1
            max_length[0] = max(res, max_length[0])
            return res
        helper(root)
        return max_length[0]

    def longestConsecutive2(self, root):
        '''
        Using BFS
        :param root:
        :return:
        '''
        if not root:
            return 0
        q = deque([[root, 1]])
        max_length = 0
        while q:
            root, length = q.popleft()
            max_length = max(max_length, length)
            if root.left:
                if root.left.val == root.val + 1:
                    q.append([root.left, length + 1])
                else:
                    q.append([root.left, 1])
            if root.right:
                if root.right.val == root.val + 1:
                    q.append([root.right, length + 1])
                else:
                    q.append([root.right, 1])
        return max_length

root = TreeNode(1)
root.left = TreeNode(2)
res = Solution().longestConsecutive(root)
print(res)
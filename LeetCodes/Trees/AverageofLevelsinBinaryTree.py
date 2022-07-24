"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
import numpy as np

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if root is None:
            return res
        Q = [root]

        while Q:
            roots_children = []
            cur = []
            while Q:
                root_cur = Q.pop(0)
                cur.append(root_cur.val)
                if root_cur.left is not None:
                    roots_children.append(root_cur.left)
                if root_cur.right is not None:
                    roots_children.append(root_cur.right)
            res.append(np.mean(np.array(cur, dtype='f')))
            Q.extend(roots_children)
        return res
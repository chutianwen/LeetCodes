"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""

from TreeNode import TreeNode
import sys
class Solution(object):
    def largestValues2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        Q = [root]

        while Q:
            roots_children = []
            max_v = -sys.maxsize - 1
            while Q:
                root_cur = Q.pop(0)
                max_v = max(max_v, root_cur.val)
                if root_cur.left is not None:
                    roots_children.append(root_cur.left)
                if root_cur.right is not None:
                    roots_children.append(root_cur.right)
            res.append(max_v)
            Q.extend(roots_children)
        return res


    def largestValues(self, root):

        def driver(root, max_v, depth):

            if root is None:
                return
            else:
                if depth not in max_v:
                    max_v[depth] = root.val
                else:
                    max_v[depth] = max(max_v[depth], root.val)
                driver(root.left, max_v, depth + 1)
                driver(root.right, max_v, depth + 1)

        max_v = {}
        driver(root, max_v, 0)
        return max_v.values()

    def findValueMostElement3(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes
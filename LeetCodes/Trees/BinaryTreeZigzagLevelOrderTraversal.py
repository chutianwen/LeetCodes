"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from collections import deque
from TreeNode import TreeNode
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        else:
            Q = deque()
            Q.append(root)
            isRightToLeft = -1
            while Q:
                res.append([])
                childs = deque()
                while Q:
                    node = Q.popleft()
                    if isRightToLeft == 1:
                        res[-1].insert(0, node.val)
                    else:
                        res[-1].append(node.val)
                    if node.left:
                        childs.append(node.left)
                    if node.right:
                        childs.append(node.right)
                isRightToLeft *= -1

                Q.extend(childs)
            return res

root = TreeNode(1)
res = Solution().zigzagLevelOrder(root)

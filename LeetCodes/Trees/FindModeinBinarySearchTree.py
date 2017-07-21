"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to
recursion does not count).
"""
from TreeNode import TreeNode
class Solution(object):
    def findMode(self, root):
        """
        Using inorder traversal on bst, return an ordered list.
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = []
        self.pre_max = 0
        self.cnt = 0

        def driver(root):
            if root:
                driver(root.left)
                if not cur:
                    cur.append(root.val)

                if cur[0] == root.val:
                    self.cnt += 1
                else:
                    cur[0] = root.val
                    self.cnt = 1

                if self.pre_max == self.cnt:
                    res.append(root.val)
                elif self.pre_max < self.cnt:
                    while res:
                        res.pop()
                    res.append(root.val)
                    self.pre_max = self.cnt
                driver(root.right)

        driver(root)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
res = Solution().findMode(root)
print(res)

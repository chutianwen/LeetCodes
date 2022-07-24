"""
Construct Binary Tree from Inorder and Postorder Traversal
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.


"""
from TreeNode import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            cur = postorder.pop()
            root = TreeNode(cur)
            id = inorder.index(cur)
            root.right = self.buildTree(inorder[id + 1:], postorder)
            root.left = self.buildTree(inorder[:id], postorder)
            return root


inorder = [1, 2, 4, 6, 7, 8, 10, 11]
postorder = [1, 2, 6, 4, 8, 11, 10, 7]
res = Solution().buildTree(inorder, postorder)


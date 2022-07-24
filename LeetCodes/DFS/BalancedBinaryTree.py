"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.
"""



from TreeNode import TreeNode

class Solution(object):
    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False
        else:
            isBalancedLeft = self.isBalanced(root.left)
            isBalancedRight = self.isBalanced(root.right)
            return isBalancedLeft and isBalancedRight

    def isBalanced(self, root):

        def helper(root):

            if root is None:
                return 0
            else:
                left = helper(root.left)
                right = helper(root.right)
                if left == -1 or right == -1 or abs(right - left) > 1:
                    return -1
                else:
                    return max(left, right) + 1
        return helper(root) != -1
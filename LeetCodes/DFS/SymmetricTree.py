"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

from TreeNode import TreeNode

class Solution(object):
    def isSymmetric(self, root):
        """
        When need to compare left and right part at same level together, than separate original tree to several subTrees
        is a solution.
        :type root: TreeNode
        :rtype: bool
        """

        def helper(p1, p2):
            if p1 and p2:
                return p1.val == p2.val and helper(p1.left, p2.right) and helper(p1.right, p2.left)
            else:
                return p1 is p2

        if root is None:
            return True
        else:
            return helper(root.left, root.right)


    def isSymmetricIterative(self, root):
        """
        Using iterative
        :param root:
        :return:
        """
        if root is None:
            return True
        p1 = root.left
        p2 = root.right
        if p1 and p2 and p1.val == p2.val:
            s1 = [p1, p2]
        else:
            return p1 is p2

        while len(s1) > 0:

            right = s1.pop()
            left = s1.pop()

            if left.left and right.right and left.left.val == right.right.val:
                s1.append(left.left)
                s1.append(right.right)
            else:
                if left.left is not right.right:
                    return False

            if left.right and right.left and left.right.val == right.left.val:
                s1.append(left.right)
                s1.append(right.left)
            else:
                if left.right is not right.left:
                    return False

        return True


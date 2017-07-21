"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
 is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

class Solution(object):
    def convertBST(self, root):
        """
        traversing from right to left, cur.val += cur.right.val
        Using two traverse, one inorder, one reversed inorder.
        :type root: TreeNode
        :rtype: TreeNode
        """
        def driver(root):
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return root.val
            else:
                root.val += self.convertBST(root.right)
                root.left.val += root.val
                self.convertBST(root.left)
                return root.right.val
        driver(root)
        return root

    def convertBST(self, root):
        inorder = []
        def visit(root):
            if root:
                visit(root.left)
                inorder.append(root.val)
                visit(root.right)

        visit(root)

        s = [0]
        def visit2(root):
            if root:
                visit2(root.right)
                s[0] += inorder.pop()
                root.val = s[0]
                visit2(root.left)
        visit2(root)
        return root

def fun():
    s = 1
    def fun2():
        s = s + 1
        print(s)
    fun2()
fun()
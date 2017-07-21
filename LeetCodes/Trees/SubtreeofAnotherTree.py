"""
iven two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def isSame(p, q):
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return p is q

        if s is None:
            return False
        else:
            # res = isSame(s, t)
            # if res:
            #     return True
            # else:
            #     return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
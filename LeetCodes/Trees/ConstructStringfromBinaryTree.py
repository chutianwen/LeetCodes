"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis
pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and
 the output.

"""
from TreeNode import TreeNode
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = ""
        if t is None:
            return res
        else:
            str_left = self.tree2str(t.left)
            str_right = self.tree2str(t.right)
            if str_right != "":
                res = "{}({})({})".format(t.val, str_left, str_right)
            else:
                if str_left != "":
                    res = "{}({})".format(t.val, str_left)
                else:
                    res = "{}".format(t.val)
            return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right =TreeNode(4)

res = Solution().tree2str(root)
print(res)
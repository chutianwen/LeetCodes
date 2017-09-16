from TreeNode import TreeNode

class Solution:

    def in_order_traversal(self, root):
        '''

        :param root: TreeNode
        :return:
        '''
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res


    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res
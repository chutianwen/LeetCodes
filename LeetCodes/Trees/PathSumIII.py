"""

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
 (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""

from TreeNode import TreeNode

class Solution(object):
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def driver(root, sums, sum):

            if root is None:
                return 0
            else:
                cnt = sums.count(root.val)
                cnt += driver(root.left, [sum - root.val for sum in sums] + [sum], sum)
                cnt += driver(root.right, [sum - root.val for sum in sums] + [sum], sum)
                return cnt
        return driver(root, [sum], sum)

    def pathSum(self, root, sum):

        def driver(root, target, cur_sum, sums):
            """

            :param root:
            :param target:
            :param cur:
            :param sums: set()
            :return:
            """

            cnt = 0
            if root is None:
                return 0
            else:
                cur_sum += root.val
                if cur_sum - target in sums:
                    cnt += sums[cur_sum - target]

                if cur_sum not in sums:
                    sums[cur_sum] = 1
                else:
                    sums[cur_sum] += 1
                cnt += driver(root.left, target, cur_sum, sums)
                cnt += driver(root.right, target, cur_sum, sums)
                # back propagation here.
                sums[cur_sum] -= 1
                return cnt
        # in case the cur_sum is the target
        sums = {0: 1}

        return driver(root, sum, 0, sums)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
# root.right.right = TreeNode(1)
# root.right.left = TreeNode(1)
res = Solution().pathSum(root, 1)
print(res)

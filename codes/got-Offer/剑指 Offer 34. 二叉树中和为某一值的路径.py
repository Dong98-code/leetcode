
"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为
输入整数的所有路径。从树的根节点开始往下一直到
叶节点所经过的节点形成一条路径。
"""
import collections
import copy
from utils_1.BinaryTree import *
nums = [7,0,None,-1,-6,None,1,None,None,-7]

tree = creat_tree(nums)

class Solution:
    def pathSum(self, root: TreeNode, target: int):
        # if not root:
        #     return []
        # queue = collections.deque()
        # queue.append((root, [root.val]))
        # ans = []
        # while queue:
        #     tmp = []
        #     node, route = queue.popleft()
        #     if not node.left and not node.right:
        #         if sum(route) == target:
        #             ans.append(route)
        #     if node.left:
        #         r1 = copy.copy(route)
        #         r1.append(node.left.val)
        #         queue.append((node.left, r1))
        #     if node.right:
        #         r2 = copy.copy(route)
        #         r2.append(node.right.val)
        #         queue.append((node.right, r2))
        # return ans
        path = []
        ans = []

        def dfs(node, target):
            if not node:
                return []
            path.append(node.val)
            target -= node.val

            if not node.left and not node.right and target == 0:
                ans.append(path[:])
            if node.left:
                dfs(node.left, target)
            if node.right:
                dfs(node.right, target)
            path.pop()
        dfs(root, target)
        return ans

sol = Solution()
print(sol.pathSum(tree, 0))

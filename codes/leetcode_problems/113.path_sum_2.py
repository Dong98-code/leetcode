from codes.utils.draw_tree import *
from codes.utils.BinaryTree import *
"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
"""

# Definition for a binary tree node.
nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
tree = creat_tree(nums)
draw(tree)
# targetSum=22


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int):
#         if not root:
#             return []
#         # lst = []
#         path = [root.val]
#         path_out=[]
#         queue = [(root, root.val, path)]
#         while queue:
#             cur_node, sum, cur_path = queue.pop(0)
#             if not cur_node.left and not cur_node.right:
#                 # cur_path.append(cur_node.val)
#                 if sum == targetSum:
#                     path_out.append(cur_path)
#
#             if cur_node.left:
#                 cur_path_left = copy.copy(cur_path)
#                 cur_path_left.append(cur_node.left.val)
#                 queue.append((cur_node.left, cur_node.left.val+sum, cur_path_left))
#             if cur_node.right:
#                 cur_path_right = copy.copy(cur_path)
#                 cur_path_right.append(cur_node.right.val)
#                 queue.append((cur_node.right, cur_node.right.val+sum, cur_path_right))
#         return path_out

"""
深度优先
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        path = []
        ret = []
        def dfs(root, targetSum):
            if not root:
                return []
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            if root.left:
                dfs(root.left, targetSum)
            if root.right:
                dfs(root.right, targetSum)
            path.pop()
            # 注意最后，当不符合要求是，现在的path里装的所有的路径，记得pop出去
        dfs(root, targetSum)
        return ret




s = Solution()
print(s.pathSum(tree, targetSum=22))

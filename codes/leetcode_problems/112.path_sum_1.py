from codes.utils.BinaryTree import *
"""
路径总和
给你二叉树的根节root 和一个表示目标和的整数targetSum 
，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点
值相加等于目标和targetSum 。

叶子节点 是指没有子节点的节点。

"""
# Definition for a binary tree node.
nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = creat_tree(nums)
# draw_graph(tree)
targetSum = 22

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root:
#             return False
#         lst = []
#         queue = [(root, root.val)]
#         while queue:
#             cur_node, sum = queue.pop(0)
#             if not cur_node.left and not cur_node.right:
#                 lst.append(sum)
#             if cur_node.left:
#                 queue.append((cur_node.left, cur_node.left.val+sum))
#             if cur_node.right:
#                 queue.append((cur_node.right, cur_node.right.val+sum))
#
#         if targetSum in lst:
#             return True
#         else:
#             return False


"""

解法二递归算法
"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
s = Solution()
print(s.hasPathSum(tree, targetSum))

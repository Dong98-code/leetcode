from codes.utils.BinaryTree import *
"""
二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
"""
lst = [2,None,3,None,4,None,5,None,6]
tree = creat_tree(lst)
draw_graph(tree)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         elif not root.right and not root.left:
#             return 1
#         min_depth = 10 ** 9
#         if root.left:
#             min_depth = min(self.minDepth(root.left), min_depth)
#         if root.right:
#             min_depth = min(self.minDepth(root.right), min_depth)
#
#         return min_depth + 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        # 引入一个队列来帮忙记录节点的深度，找到第一个叶子节点，直接返回其深度，先入队在出队
        while queue:
            node, depth = queue.pop(0)
            if not node.left and not node.right:
                return depth
            # 对出队的元素进行判断，如果为叶子节点直接返回depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return 0
s = Solution()
print(s.minDepth(tree))

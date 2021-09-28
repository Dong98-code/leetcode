"""
给定一棵二叉搜索树，请找出其中第k大的节点。

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
"""
from utils_1.BinaryTree import *
from utils_1.draw_tree import *
nums = root = [3,1,4,None, 2]
tree = creat_tree(nums)
# draw(tree)
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root, k):
        # lst = []
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            # lst.append(root.val)
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

sol = Solution()
print(sol.kthLargest(tree,3))

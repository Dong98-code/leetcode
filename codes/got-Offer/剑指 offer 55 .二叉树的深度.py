"""

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""
from utils_1.BinaryTree import *
from utils_1.draw_tree import *
nums = [3, 9, 20, None, None,15,7]
tree = creat_tree(nums)
# draw(tree)
import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_dep = 1

        queue =collections.deque()
        queue.append((root,1))
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                max_dep = max(max_dep, depth)
            if node.left :
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return max_dep

sol = Solution()
print(sol.maxDepth(tree))

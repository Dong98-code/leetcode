from codes.utils.draw_tree import *
from codes.utils.BinaryTree import *

nums = [1, 2, 5, 3, 4, None, 6]
tree = creat_tree(nums)
draw(tree)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur_node = root
        while cur_node:
            if cur_node.left:
                pre_node = next_node = cur_node.left
                while pre_node.right:
                    pre_node = pre_node.right
                pre_node.right = cur_node.right
                cur_node.left = None
                cur_node.right = next_node


            cur_node = cur_node.right
        return root

s = Solution()
tree0 = s.flatten(tree)


# Definition for a binary tree node.
from utils.draw_tree import *



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # def height(root):
        #     if not root:
        #         return 0
        #     left_height = height(root.left)
        #     right_height = height(root.right)
        #     if left_height == -1 or right_height==-1 or abs(left_height-right_height) >1:
        #         return -1
        #     else:
        #         return max(left_height, right_height)+1
        # return height(root) >= 0
        def height(root):
            if not root:
                return 0
            else:
                return max(height(root.left), height(root.right))+1
        if not root:
            return True
        return  abs(height(root.left)-height(root.right)) <= 1 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)



lst =[3, 9, 20, None, None, 15, 7]
tree = creat_tree(lst)
# draw_graph(tree)
s = Solution()
print(s.isBalanced(tree))

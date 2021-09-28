class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:  # prev 用于判断右节点是否遍历过
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

from utils.BinaryTree import *
nums = [1, 4, 2, 3]
root = creat_tree(nums)
sol = Solution()
print(sol.postorderTraversal(root))

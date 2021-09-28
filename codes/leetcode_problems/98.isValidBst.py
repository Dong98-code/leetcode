# -*- coding: utf-8 -*-
# @Time : 2021/7/17 12:05
# @Author : XDD
# @File : 98.isValidBst.py
from codes.utils.BinaryTree import *
nums =  [1,2,3]
root = creat_tree(nums)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


sol = Solution()
print(sol.isValidBST(root))


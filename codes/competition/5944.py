# -*- coding: utf-8 -*-
# @Time : 2021/12/5 11:58
# @Author : XDD
# @File : 5944.py
# Definition for a binary tree node.

class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def getLatCommnAncetor(root, startValue, destValue):
            # A&B=>LCA
            # !A&!B=>None
            # A&!B=>A
            # B&!A=>B
            if (root is None or root.val == startValue or root.val == destValue):
                return root  # 若root为空或者root为A或者root为B，说明找到了A和B其中一个
            left = getLatCommnAncetor(root.left, startValue, destValue)
            right = getLatCommnAncetor(root.left, startValue, destValue)
            if (left is not None and right is not None):
                return root  # 若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
            if (left is None):  # 若左子树是none右子树不是，说明右子树找到了A或B
                return right
            if (right is None):  # 同理
                return left
            return None

        def getPath(root, val):
            # 从目标树节点，找到到目标值的路径
            if not root:
                return []
            pathList, stack = [], [(root, "")]
            while stack:
                node, pathStr = stack.pop(0)
                if node.val == val:
                    return pathStr
                if node.left:
                    stack.append((node.left, pathStr + 'L'))
                if node.right:
                    stack.append((node.right, pathStr + 'R'))
            return pathList

        # 先找到公共节点
        commn_father = getLatCommnAncetor(root, startValue, destValue)
        res = ""

        if commn_father.val != startValue and commn_father.val != destValue:
            path_s = getPath(commn_father, startValue)
            path_d = getPath(commn_father, destValue)
            for i in range(len(path_s)):
                res += 'U'
            res += path_d
        elif commn_father.val == startValue:
            res = getPath(commn_father, destValue)
        else:
            path_s = getPath(commn_father, startValue)
            for i in range(len(path_s)):
                res += 'U'
        return res

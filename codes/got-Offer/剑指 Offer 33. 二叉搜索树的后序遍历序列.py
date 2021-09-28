"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回
true，否则返回
false。假设输入的数组的任意两个数字都互不相同。

"""

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 递归
        if not postorder:
            return True
        root = postorder[-1]
        length = len(postorder)
        p = 0  # 第一个最大值的索引
        for i in range(length):
            if postorder[p] < root:
                p += 1
        for i in range(p, length-1):
            if postorder[i] < root:
                return False
        return self.verifyPostorder(postorder[0: p]) and self.verifyPostorder(postorder[p: length-1])

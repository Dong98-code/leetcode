from codes.utils.BinaryTree import *
nums = [4,2,7,1,3]
root = creat_tree(nums)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # if not root:
        #     return TreeNode(val)
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # if val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
        ## 迭代， 迭代的方法需要遍历，需要维持一个父节点的值
        if not root:
            return TreeNode(val)
        f_node = root  # 父节点
        cur = root
        while cur:
            f_node = cur
            if val > cur.val:
                cur = cur.right
            elif val < cur.val:
                cur = cur.left

        if val > f_node.val:
            f_node.right = TreeNode(val)
        else:
            f_node.left = TreeNode(val)
        return root


sol = Solution()
print(sol.insertIntoBST(root, 5))

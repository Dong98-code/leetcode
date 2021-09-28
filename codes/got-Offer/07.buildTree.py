"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        # 1.根据前序遍历确树的根节点
        # 2. 根据中序遍历顺序 找到两个子树的集合
        if not preorder or not inorder:
            return None
        root_val = preorder[0] # 根节点的值
        root = TreeNode(root_val) #根节点创建node
        index_root = inorder.index(root_val)
        inorder_left_subtree = inorder[:index_root]
        inorde_right_subtree = inorder[index_root+1:]
        preorder_left_subtree = preorder[1:1+len(inorder_left_subtree)]
        preorder_rigth_subtree = preorder[-len(inorde_right_subtree):]
        root.left = self.buildTree(preorder_left_subtree,inorder_left_subtree)
        root.right =self.buildTree(preorder_rigth_subtree, inorde_right_subtree)
        return root

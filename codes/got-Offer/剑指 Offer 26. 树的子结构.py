"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creat_tree(node_list):
    if node_list[0] is None:
        return None
    root = TreeNode(node_list[0])
    # 根节点
    nodes = [root]
    # 节点的列表,
    j = 1
    for node in nodes:
        if node is not None:
            node.left = (TreeNode(node_list[j]) if node_list[j] is not None else None)
            nodes.append(node.left)
            j += 1
            if j == len(node_list):
                return root
            node.right = (TreeNode(node_list[j])if node_list[j] is not None else None)
            j += 1
            nodes.append(node.right)
            if j == len(node_list):
                return root

A = [1,2,3]
B = [3,1]
tree_a = creat_tree(A)
tree_b = creat_tree(B)




class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        def rec(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return rec(A.left, B.left) and rec(A.right, B.right)
        return rec(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


sol = Solution()
print(sol.isSubStructure(tree_a, tree_b))



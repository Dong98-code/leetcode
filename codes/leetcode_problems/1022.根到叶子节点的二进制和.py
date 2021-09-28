from codes.utils.BinaryTree import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        # 深度优先，递归
        def dfs(node, sum_cur):
            if not node:
                return 0
            sum_cur = 2*sum_cur+node.val
            while not node.left and not node.right:
                return sum_cur
            return dfs(node.left, sum_cur)+dfs(node.right, sum_cur)
        return dfs(root, 0)


if __name__ == "__main__":
    root = [1, 0, 1, 0, 1, 0, 1]
    tree = creat_tree(root)
    # draw(tree)
    solution = Solution()
    print(solution.sumRootToLeaf(tree))

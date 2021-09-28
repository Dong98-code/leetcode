# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        if(n == 0):
            return []
        def build_Trees(left,right):
            all_trees=[]
            if(left> right):
                return [None]
            for i in range(left, right+1):
                left_trees=build_Trees(left, i-1)
                right_trees=build_Trees(i+1, right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees
        res=build_Trees(1, n)
        return res

sol = Solution()
print(sol.generateTrees(3))

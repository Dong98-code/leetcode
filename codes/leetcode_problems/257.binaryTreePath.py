class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import copy
import collections
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        queue = collections.deque()
        queue.append((root, [root.val]))
        ans = []
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                path_tmp = ""
                for i in range(len(path) - 1):
                    path_tmp = path_tmp + str(path[i]) + "->"
                path_tmp = path_tmp + str(path[-1])
                ans.append(path_tmp)
            if node.left:
                path_l = copy.copy(path)
                path_l.append(node.left.val)
                queue.append((node.left, path_l))
            if node.right:
                path_r = copy.copy(path)
                path_r.append(node.right.val)
                queue.append((node.right, path_r))
        return ans

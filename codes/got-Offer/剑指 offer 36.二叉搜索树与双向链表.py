from utils_1.BinaryTree import *
from utils_1.draw_tree import *
nums = [4, 2, 5, 1, 3]
tree = creat_tree(nums)
# draw(tree)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return []
        def f(cur):
            if not cur:
                return
            f(cur.left)
            if self.pre :
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur
            self.pre = cur
            f(cur.right)
        self.pre = None

        f(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

sol = Solution()
print(sol.treeToDoublyList(tree))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                return None

            mid = (left+right)//2
            o = TreeNode(nums[mid])
            o.left = helper(left, mid-1)
            o.right = helper(mid+1, right)
            return o
        return helper(0, len(nums)-1)
s = Solution()
nums = [1, 3]
tree = s.sortedArrayToBST(nums)

draw_graph(tree)


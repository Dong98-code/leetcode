"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permute(self, nums):
        path = []
        res = []
        uesd = [0] * len(nums)

        def backtrack(nums, uesed):
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if uesd[i]:
                    continue
                uesd[i] = 1
                path.append(nums[i])
                backtrack(nums, uesd)
                uesd[i] = 0
                path.pop()

        backtrack(nums, uesd)
        return res

sol = Solution()
print(sol.permute([1,2,3]))


"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""

class Solution:
    def permuteUnique(self, nums):
        path = []
        res = []
        uesd = [0] * len(nums)

        def backtrack(nums, uesed):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # 剪枝的条件
                if (i>0 and uesd[i] == uesd[i-1] and not uesd[i-1]):
                    continue
                # if uesd[i]:
                #     continue
                uesd[i] = 1
                path.append(nums[i])
                backtrack(nums, uesd)
                uesd[i] = 0
                path.pop()

        backtrack(nums, uesd)
        return res
nums = [1,1,2]
sol =Solution()
print(sol.permuteUnique(nums))

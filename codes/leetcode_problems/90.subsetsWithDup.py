"""
90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。



示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        path = []

        def backtrack(k, start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, len(nums)):  # i为nums中的数字的索引
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(k, i + 1)
                path.pop()

        for k in range(len(nums) + 1):
            backtrack(k, 0)
        return res
sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))

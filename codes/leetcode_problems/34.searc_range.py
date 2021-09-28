"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
"""
class Solution:
    def searchRange(self, nums, target: int) :
        # # 双指针
        # if not nums:
        #     return [-1, -1]
        #
        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         tmp_l = mid
        #         tmp_r = mid
        #         while  tmp_l >= 0 and nums[tmp_l] == target:
        #             tmp_l -= 1
        #         while tmp_r <= len(nums) - 1 and nums[tmp_r] == target:
        #             tmp_r += 1
        #         return [tmp_l+1, tmp_r-1]
        #     if nums[mid] > target:
        #         r -= 1
        #     else:
        #         l += 1
        # return [-1, -1]
        # hash
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        if target in dic:
            return [dic[target][0], dic[target][-1]]
        else:
            return [-1, -1]


nums = [5, 7, 7, 8, 8, 10, 10]
sol = Solution()
print(sol.searchRange(nums, 10))

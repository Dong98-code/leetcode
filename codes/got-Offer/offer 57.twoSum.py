"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使
得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。


输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
双指针
"""
class Solution:
    def twoSum(self, nums, target: int) :
        p1 = 0
        p2 = len(nums)-1
        while p1<=p2:
            sum = nums[p1]+nums[p2]
            if sum > target:
                p2 -= 1
            elif sum < target:
                p1 += 1
            else:
                return [nums[p1], nums[p2]]
        return []

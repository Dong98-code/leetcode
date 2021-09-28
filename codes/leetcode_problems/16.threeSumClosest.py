"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()  # 升序排列
        ans = nums[1]+nums[2]+nums[3]
        n = len(nums)
        for i in range(n-2):
            l = i+1  # 左指针
            r = n-1  # right,右指针
            while l < r:
                tmp_sum = nums[i] + nums[l] + nums[r]
                if abs(tmp_sum-target) < abs(ans-target):
                    ans = tmp_sum
                if tmp_sum > target:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp_sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    return tmp_sum
        return ans

sol =  Solution()
nums = [-1,2,1,-4]
target = 1
print(sol.threeSumClosest(nums, target))

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
class Solution:
    def maxSubArray(self, nums) -> int:
        pre = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            if nums[i]+pre > nums[i]:
                pre = pre+nums[i]
            else:
                pre = nums[i]
            max_sum = max(max_sum, pre)
        return max_sum





if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solu = Solution()
    print(solu.maxSubArray(nums))

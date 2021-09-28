"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
"""
class Solution:
    def search(self, nums, target: int) -> int:
        # 二分
        low = 0
        high = len(nums)-1
        # if nums[0] == target:
        #     return 0
        # if nums[high] == target:
        #     return high
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
nums = [4,5,6,7,0,1,2]
sol = Solution()
print(sol.search(nums, 0))

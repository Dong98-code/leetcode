"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


"""
class Solution:
    def threeSum(self, nums):
        # # 排序，双指针
        res = []
        nums = sorted(nums)  # 升序排列
        n = len(nums)
        for i in range(n - 2):
            # 当nums[i] 》 0时，直接bresk
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = n-1
            while left < right:
                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1
                tmp_sum = nums[left] + nums[right]
                if tmp_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1 # 当 left +1之后，应该判断新的left和原来的那个的值，如果一样，继续加1
                elif tmp_sum > target:
                    right -= 1
                    while left < right and nums[right] == nums [right +1]:
                        right -= 1
                else:
                    res.append( [nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res


nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))

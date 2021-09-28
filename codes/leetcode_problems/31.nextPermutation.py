"""
31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。


"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [] or [1] return nums
        n = len(nums)
        if n <= 1:
            return nums
        i = n-1
        while i > 0:
            # 存在升序的情况
            if nums[i] > nums[i - 1]:
                reverse_strat = i
                minalt = nums[i]
                minindex = i
                for j in range(i, n):
                    if nums[j] > nums[i - 1] and nums[j] <= minalt:
                        minalt = nums[j]
                        minindex = j
                nums[i-1], nums[minindex] = nums[minindex], nums[i-1]
                break
            i -= 1
        num = ((n - reverse_strat) // 2)
        for index in range(num):
            nums[reverse_strat + index], nums[n - index - 1] = nums[n - index - 1], nums[reverse_strat + index]

sol =  Solution()
print(sol.nextPermutation([0,1,2,5,3,4]))

"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。
"""
class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            lst = nums[i:i + 3]
            if lst[2] > lst[0] - lst[1]:
                return sum(lst)
        return 0

if __name__ == "__main__":
    solu = Solution()
    nums = [2,1,2]
    print(solu.largestPerimeter(nums))

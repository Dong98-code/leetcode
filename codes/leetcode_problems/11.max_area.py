"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""
class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            volume = min(height[left], height[right]) * (right - left)
            if volume >= max_area:
                max_area = volume
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
sol = Solution()
height = [1,2,3,4]
print(sol.maxArea(height))

class Solution:
    def canJump(self, nums) -> bool:
        n = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= n:
                n = 1
            else:
                n += 1
            if i == 0 and n >1:
                return False
        return True
sol = Solution()
nums = [3,2,1,0,4]
print(sol.canJump(nums))

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for num in nums:
            if i < 2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i
sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))

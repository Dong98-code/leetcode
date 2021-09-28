class Solution:
    def search(self, nums, target: int) -> int:
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i] < target:
        #         cnt = cnt
        #     elif nums[i] == target:
        #         cnt += 1
        #     else:
        #         return cnt
        j = len(nums) - 1
        i = 0
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] <= target:
                i = mid + 1
        right = i
        i = 0
        j = right - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] >= target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
        left = j
        return right-left-1

nums = [1]
target = 1
sol = Solution()
print(sol.search(nums, 8))

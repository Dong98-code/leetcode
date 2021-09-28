class Solution:
    def frequencySort(self, nums):
        # nums.sort(reverse = True)
        ans = sorted(nums, key = lambda x : (nums.count(x), -x)) 
        return ans

if __name__ == "__main__":
    nums = [1,1,2,2,2,3]
    solu = Solution()
    print(solu.frequencySort(nums))

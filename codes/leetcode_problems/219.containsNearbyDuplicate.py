"""
219. 存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。



示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
"""
import collections
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        queue = collections.deque(maxlen=k)
        for i in range(len(nums)):
            if nums[i] in queue:
                return True
            queue.append(nums[i])
        return False
        # n = len(nums)
        # dic = {}
        # for i in range(n):
        #     if nums[i] in dic :
        #          if (i - dic[nums[i]][-1]) <= k:
        #             return True
        #          else:
        #              dic[nums[i]].append(i)
        #     else:
        #         dic[nums[i]] = [i]
        # return False



sol = Solution()
nums = [1,0,1,1]
print(sol.containsNearbyDuplicate(nums, 1))

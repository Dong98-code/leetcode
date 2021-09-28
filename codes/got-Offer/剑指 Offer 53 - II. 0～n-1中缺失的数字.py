"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每
个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] > i:
        #         return i
        # return n
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == mid:
                i = mid +1
            else:
                j = mid -1
        return i

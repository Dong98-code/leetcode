"""
228. 汇总区间
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"


"""
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return nums
        n = len(nums)
        # if n == 1:
        #     return [str(nums[-1])]
        ans = []
        start = stop = 0

        while stop < n:
            # stop = start+1
            if not (stop < n - 1 and nums[stop] + 1 == nums[stop + 1]):
                if start == stop:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start])+"->"+str(nums[stop]))
                start = stop + 1
            stop += 1

        return ans
        # n = len(nums)
        # left = right = 0
        # rst = list()
        #
        # """
        # 思路：两个指针，一个标记开头，一个标记结尾。 难点在于对 最后元素的处理，比方说 right = n-1时
        # """
        # while right < n:
        #     if not ():
        #         if left == right:
        #             rst.append(str(nums[left]))
        #         else:
        #             rst.append(str(nums[left]) + "->" + str(nums[right]))
        #         left = right + 1
        #     right += 1
        #
        # return rst

    # 作者：1501615430
    # 链接：https: // leetcode - cn.com / problems / summary - ranges / solution / liang - ge - zhi - zhen - yi - ge - biao - ji - kai - tou - c1mbo /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

sol = Solution()
nums =  [0, 2, 3, 4,6,8,9]
print(sol.summaryRanges(nums))

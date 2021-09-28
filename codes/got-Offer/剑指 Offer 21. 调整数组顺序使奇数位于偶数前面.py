"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
示：

输入：nums =[1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def exchange(self, nums):
#         ans = []
#         for i in range(len(nums)):
#             if nums[i] % 2 == 1:
#                 ans.insert(0, nums[i])
#             else:
#                 ans.append(nums[i])
#         return ans

"""
双数组

"""
# class Solution:
#     def exchange(self, nums):
#         ans1 = []
#         ans2 = []
#         for i in range(len(nums)):
#             if nums[i] % 2 == 1:
#                 ans1.append(nums[i])
#
#             else:
#                 ans2.append(nums[i])
#         return ans1 + ans2

class Solution:
    def exchange(self, nums):
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            while p1 <= p2 and nums[p1] % 2 == 1:
                p1 += 1
            while p1 <= p2 and nums[p2] % 2 == 0:
                p2 -= 1
            if p1 > p2:
                break
            nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums
sol = Solution()
nums = [1, 2, 3, 4]
print(sol.exchange(nums))


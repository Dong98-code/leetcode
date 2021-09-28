#-*- coding : utf-8-*-
# coding:unicode_escape
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def singleNumbers(self, nums):
        ret = 0
        #  得到x^y x与y的异或值，不同的哪一位，在这一位上为1
        for num in nums:
            ret ^= num
        #  寻找第一个不相同的位
        m = 1
        while m & ret == 0:
            m <<= 1
        x, y = 0, 0
        #  分组： x,y和其他的肯定时不同的，那么找到x,y不同的一位 ，和这一位相同的为一组，不同的为一组，分成两组
        for num in nums:
            if num & m == 0:
                x = x ^ num
            else:
                y = y ^ num
        return [x, y]


sol = Solution()
nums = [1,2,10,4,1,4,3,3]
print(sol.singleNumbers(nums))

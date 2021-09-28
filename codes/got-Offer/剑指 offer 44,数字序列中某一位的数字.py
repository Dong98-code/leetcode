# -*- coding:utf-8 -*-
"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findNthDigit(self, n):
        start = 1
        digit = 1
        cnt = 9
        while n > cnt:
            n -= cnt
            start = start*10
            digit += 1
            cnt = 9*start*digit
        num = start +(n-1)//digit

        return int(str(num)[(n-1) % digit])








sol = Solution()
print(sol.findNthDigit(n=3))

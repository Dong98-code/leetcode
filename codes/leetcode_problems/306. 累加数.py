# -*- coding: utf-8 -*-
# @Time : 2022/1/10 19:36
# @Author : XDD
# @File : 306. 累加数.py
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for second_start in range(1, n-1):
            if num[0] == "0" and second_start != 1:
                break
            for second_end in range(second_start, n-1):
                if num[second_start] == "0" and second_start != second_end:
                    break
                if self.valid(second_start, second_end, num):
                    return True
        return False

    def valid(self, second_start, second_end, num):
        """

        :param second_start: int
        :param second_end:int
        :param num: str
        :return: bool
        """
        n = len(num)
        first_start = 0
        first_end = second_start - 1
        while second_end <= n-1:
            third = self.string_add(num, first_start, first_end, second_start, second_end)
            third_start = second_end + 1
            third_end = second_end + len(third)
            if third_end >= n or num[third_start:third_end+1] != third:
                break
            if third_end == n-1:
                return True
            first_start, first_end = second_start, second_end
            second_start, second_end = third_start, third_end
        return False

    def string_add(self, s, first_start, first_end, second_start, second_end):
        """
        :param s: num
        :param first_start:int
        :param first_end: int
        :param second_start: int
        :param second_end: int
        :return: str
        """
        third = []
        carry, cur = 0, 0
        while first_end >= first_start or second_end >= second_start or carry != 0:
            cur = carry
            if first_end >= first_start:
                cur += ord(s[first_start]) - ord('0')
                first_end -= 1
            if second_end >= second_end:
                cur += ord(s[second_end]) - ord('0')
                second_end -= 1
            carry = cur // 10
            cur %= 10
            third.append(chr(cur + ord('0')))
        return ''.join(third[::-1])


sol = Solution()
num = "000358"
print(sol.isAdditiveNumber(num))

# -*- coding: utf-8 -*-
# @Time : 2021/11/9 10:31
# @Author : XDD
# @File : 488.祖玛游戏.py
def remove(line):
    """
    :param line: str
    :return:  消除3个连续球之后的str
    """
    count = 1
    ans = ""
    for i, ball in enumerate(line):
        if i == 0:
            ans = ball
            # i += 1
            continue
        if ball == ans[-1]:
            count += 1
        else:
            if count >= 3:
                ans = ans[:-count]
            count = 1
            j = len(ans) - 1
            while j >= 0 and ans[j] == ball:  # 删除之后，记录现在几位的情况
                j -= 1
                count += 1
        ans += ball
    if count >= 3:
        ans = ans[:-count]
    return ans

print(remove('WWRRBBBRR'))
# class Solution:
#     def findMinStep(self, board: str, hand: str) -> int:



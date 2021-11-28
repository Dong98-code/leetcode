# -*- coding: utf-8 -*-
# @Time : 2021/11/28 11:27
# @Author : XDD
# @File : 5491.知晓秘密的所有专家.py
class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        # 先按照时间升序排列
        meetings.sort(key=lambda x: x[-1])

        length = len(meetings)
        ini_set = {0, firstPerson}  # 初始节点
        i = 0
        while i < length:
            j = i + 1
            while j < length and meetings[j][-1] == meetings[i][-1]:
                j += 1

            # 从前到后，从后到前 遍历 [i,j]
            for idx in range(i, j):
                p1 = meetings[idx][0]
                p2 = meetings[idx][1]
                if p1 in ini_set or p2 in ini_set:
                    ini_set.add(p1)
                    ini_set.add(p2)
            for idx in range(j - 1, i - 1, -1):
                p1 = meetings[idx][0]
                p2 = meetings[idx][1]
                if p1 in ini_set or p2 in ini_set:
                    ini_set.add(p1)
                    ini_set.add(p2)

            i = j  # 更新i
        return list(ini_set)

n = 4
meetings = [[3,1,3],[1,2,2],[0,3,3]]
firstPerson = 3
sol = Solution()
print(sol.findAllPeople(6,meetings, firstPerson))

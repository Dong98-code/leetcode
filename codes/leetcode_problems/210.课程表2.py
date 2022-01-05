# -*- coding: utf-8 -*-
# @Time : 2022/1/5 17:04
# @Author : XDD
# @File : 210.课程表2.py
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites):

        # 建图
        graph = []
        deg_in = [0] * numCourses
        for i in range(numCourses):
            graph.append([])
        # 遍历 prerequistes
        for pre in prerequisites:
            u, v = pre
            graph[v].append(u)  # v ->u
            deg_in[u] += 1

        q = collections.deque()
        for i in range(numCourses):
            if deg_in[i] == 0:
                q.append(i)  # 此时i的入度为0

        res = []
        while q:
            node = q.popleft()
            # 此时学习完了 ，对应的后续课程的入度-1
            res.append(node)
            for head in graph[node]:
                if deg_in[head] == 0:
                    q.append(head)
                deg_in[head] -= 1
                if deg_in[head] == 0:
                    q.append(head)
        if len(res) != numCourses:
            return []
        return res


sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses=4, prerequisites=prerequisites))

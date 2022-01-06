# -*- coding: utf-8 -*-
# @Time : 2022/1/6 23:29
# @Author : XDD
# @File : 207.课程表.py
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # 判断 是否有环
        # 第一步建图  课程为 索引
        graph = collections.defaultdict(list)
        deg_in = [0] * numCourses  # 记录每一个课程得入度
        for pre in prerequisites:
            u, v = pre
            graph[v].append(u)  # 0 -> 1
            deg_in[u] += 1  # 入度 + 1

        # 将入度为0得课加入到 队列
        q = collections.deque()
        for i in range(numCourses):
            if deg_in[i] == 0:
                q.append(i)  # 索引与课程相对应
        # res = []  # 表示能学习到的课程
        res = 0
        while q:
            tail = q.popleft()
            # res.append(tail)
            res += 1
            for head in graph[tail]:
                # 遍历以tail为tail 指向 head
                # 将对应的head 的入度 -1
                deg_in[head] -= 1
                if deg_in[head] == 0:
                    # 表示学习完了该课程
                    # res.append(head)
                    q.append(head)  # 该节点入度wei0
        return res == numCourses  # 如果不等，说明存在环


sol = Solution()
pre = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
print(sol.canFinish(20, prerequisites=pre))

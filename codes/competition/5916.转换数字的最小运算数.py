# -*- coding: utf-8 -*-
# @Time : 2021/10/31 13:18
# @Author : XDD
# @File : 5916.转换数字的最小运算数.py
import collections

class Solution:
    def minimumOperations(self, nums, start: int, goal: int) -> int:
        # 广度优先
        queue = collections.deque() # 双端队列
        queue.append(start)
        # visited = defaultdict(bool)  # 默认返回值的字典
        # 使用set
        visited = set()
        now_step = 1
        while len(queue) != 0:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for num in nums:
                    plus = cur + num
                    minus = cur - num
                    xor = cur ^ num
                    if plus == goal or minus == goal or xor == goal:
                        return now_step
                    if plus >= 0 and plus <= 1000 and plus not in visited:
                        visited.add(plus)
                        queue.append(plus)
                    if minus >=0 and minus <= 1000 and minus not in visited:
                        visited.add(minus)
                        queue.append(minus)
                    if xor >= 0 and minus <= 1000 and xor not in visited:
                        visited.add(xor)
                        queue.append(xor)
            now_step += 1
        return -1

sol = Solution()
nums = [-821076380,-675066150,-306144249,504919653,716238043,-124990086,-428244973,655635118,-685309701,-829855358,-383651019,-469183737,481606536,60542672,70931791,16572795,245816770,-764645310,149691790,350230253,306994852,189683672,999272836,811531837,-666576311,-612033029,649577485]
start = 495
goal = -416969045
print(sol.minimumOperations(nums, start, goal))

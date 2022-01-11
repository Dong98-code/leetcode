# -*- coding: utf-8 -*-
# @Time : 2022/1/11 16:24
# @Author : XDD
# @File : 1036.逃离大迷宫.py
import collections
class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        # 分别表示 在包围圈内；不在包围圈内；在不在已经找到
        block = -1
        valid = 0
        found = 1
        boundary = 10 ** 6

        if len(blocked) < 2:
            return True

        hash_blocked = set(tuple(pos) for pos in blocked)  # set()

        # BFS
        def check(hash_blocked, source, target):
            count = len(blocked) * (len(blocked) - 1) // 2
            s_x, s_y = source
            t_x, t_y = target
            q = collections.deque()
            q.append((s_x, s_y))
            visited = set()
            visited.add((s_x, s_y))  # 已经访问过的点

            # BFS
            while q and count > 0:
                x, y = q.popleft()  # 从此点开始搜索
                for x_n, y_n in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= x_n < boundary and 0 <= y_n < boundary and (x_n, y_n) not in hash_blocked and (
                    x_n, y_n) not in visited:
                        if (x_n, y_n) == (t_x, t_y):
                            return found
                        count -= 1
                        q.append((x_n, y_n))
                        visited.add((x_n, y_n))
            if count > 0:
                return block
            return valid  # 此时不在包围圈内

        result_1 = check(hash_blocked, source, target)
        if result_1 == found:
            return True
        elif result_1 == block:  # 此时被困住，但是 还没有找到目标点
            return False
        else:
            result_2 = check(hash_blocked, target, source)
            if result_2 == block:
                return False
            return True


sol = Solution()
blocked = [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
source = [655988,180910]
target = [267728,840949]
print(sol.isEscapePossible(blocked, source, target))

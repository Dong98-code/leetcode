# -*- coding: utf-8 -*-
# @Time : 2021/12/16 15:35
# @Author : XDD
# @File : 1610.可见点的最大数目.py
import math
class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:
        # 首先计算 每一个点与坐标点的夹角
        def get_angle(point, location):
            p_x = point[0]
            p_y = point[1]
            l_x = location[0]
            l_y = location[1]
            return math.atan2(p_y - l_y, p_x - l_x) * 180 / math.pi

        angles = []
        loc_num = 0
        for i in range(len(points)):
            if points[i] == location:
                loc_num += 1
            else:
                angles.append(get_angle(points[i], location))
        # angles 为 每一个点与 loc的夹角
        max_point = 0
        angles.sort()
        angles += [angle + 2 * math.pi for angle in angles]
        for i in range(len(angles)):
            p = i
            while p < len(angles) and angles[p] <= angles[i] + angle:
                p += 1
            max_point = max(max_point, p - i)
        return max_point + loc_num

sol = Solution()
points = [[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]]
angle = 0
location = [1,1]
print(sol.visiblePoints(points, angle, location))

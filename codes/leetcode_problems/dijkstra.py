# -*- coding: utf-8 -*-
# @Time : 2021/11/3 20:44
# @Author : XDD
# @File : dijkstra.py
# 函数：Dijkstra算法
#
finite = float('inf')
def dijkstra(graph, start, end):
    points = len(graph)
    pre = [0] * (points)  # 记录前驱， 用于记录路径
    vis = [0] * (points)  # 记录节点遍历状态
    dis = [finite for i in range(points)]  # 保存最短距离
    road = [0] * (points)  # 保存最短路径
    roads = []

    # 初始化起点到其他点的距离
    for i in range(points):
        if i == start:
            dis[i] = 0
        else:
            dis[i] = graph[start][i]
        if graph[start][i] != finite:
            pre[i] = start  # 此时出发几点出发，可以到达节点i 节点i的前驱节点就是start
        else:
            pre[i] = -1
    vis[start] = 1  # 此时，start 已经访问过了，

    # 每次循环确定一条最短路
    for i in range(points):
        minimum = finite
        # 确定当前最短路
        for j in range(points):
            if vis[j] == 0 and dis[j] < minimum:  # 该点当前还没有访问过
                t = j
                minimum = dis[j]
                # 找到并标记最短的一条路径
        vis[t] = 1
        # 将所有没有 访问过的点中的距离最短的点设为t
        for j in range(points):
            if vis[j] == 0 and dis[j] > dis[t] + graph[t][j]:
                dis[j] = dis[t] + graph[t][j]
                pre[j] = t
    p = end
    length = 0
    while p >= 0 and length < points:
        road[length] = p
        p = pre[p]
        length += 1
    length -= 1
    while length >= 0:
        roads.append(road[length])
        length -= 1
    return dis[end], roads
# 定义路网连通图

graph=[[finite, 2, finite, 4, 7, finite],
       [finite, finite, 2, finite, 5, finite],
       [finite, finite, finite, finite, finite, 3],
       [finite, finite, finite, finite, 4, finite],
       [finite, finite, 3, finite, finite, 1],
       [finite, finite, finite, finite, finite, finite],
       ]
# 输入起点和终点
r, s = input("输入起点和终点：").split()
dis, road = dijkstra(graph, int(r), int(s))
# 输出最短路结果
print("最短路径：", road)
print("最短距离：", dis)

# dijkstra 最短路径法

目的：给出图及邻接关系，求出给定的源点到图上其他点的最短路径

```text
邻接表形式的联通图
1 2 5
1 3 8
2 3 1
2 4 3
4 5 7
2 5 2
点 点 权重
```
Dijkstra 算法是一种类似于贪心的算法，步骤如下：

1、当到一个时间点时，图上部分的点的最短距离已确定，部分点的最短距离未确定。

2、选一个所有未确定点中离源点最近的点，把他认为成最短距离。

3、再把这个点所有出边遍历一边，更新所有的点。

## 具体流程

首先建立一个dis[] 表示点i到源点的 估计最短距离

建立邻接矩阵 `map[i][j]` 从i到j的权重为v

`dis`初始值 除源点本身为0外，其余值均为1

先从1号点开始。一号点，`map[1][2]=5`,一号点离2号点是5，比无穷大要小，所以dis[2]从无穷大变成了5。顺便，我们用minn记录距离1号点最短的点，留着以后会用。

`dis[0,5,∞,∞,∞]`。`minn=2`。
第二步：

现在，dis数组所呈现的明显不是最终答案，因为我们才更新一遍，现在我们开始第二次更新，第二次更新以什么为开始呢？

就是以上一次我们存下来的，minn，相当于把2当源点，求所有点到它的最短路，加上它到真正的源点（1号点）的距离，就是我们要求的最短路。


从2号点开始，搜索3号点，map[2][3]=1，原本dis[3]=8，发现dis[2]+map[2][3]=5+1=6<dis[3](8)所以更新dis[3]为6，minn=3dis[0,5,6,∞,∞] minn=3.


然后搜索4号点，map[2][4]=3,原本dis[4]=∞,所以，dis[2]+map[2][4]=5+3=8<dis[4](∞)所以更新dis[4]=8,因为map[2][4]=3,3>1,minn不更新。

dis[0,5,6,8,∞] minn=3.


接着搜索5号点，map[2][5]=2,5+2=7,7<∞,dis[5]=7minn不变。

dis[0,5,6,8,7]

## 最小堆优化
```python
import time
def dijkstra(G,start):     ###dijkstra算法    
    INF = 999999999
 
    dis = dict((key,INF) for key in G)    # start到每个点的距离
    dis[start] = 0
    vis = dict((key,False) for key in G)    #是否访问过，1位访问过，0为未访问
    ###堆优化
    pq = []    #存放排序后的值
    heapq.heappush(pq,[dis[start],start])
 
    t3 = time.time()
    path = dict((key,[start]) for key in G)    #记录到每个点的路径
    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
        if vis[v] == True:  # 在此判断是否访问过
            continue
        vis[v] = True
        p = path[v].copy()    #到v的最短路径
        for node in G[v]:    #与v直接相连的点
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node] and (not vis[node]):    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis    #更新点的距离
              #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                heapq.heappush(pq,[dis[node],node])
                temp = p.copy()
                temp.append(node)    #更新node的路径
                path[node] = temp    #将新路径赋值给temp
 
    t4 = time.time()
    print('Dijkstra算法所用时间:',t4-t3)
    return dis,path
```


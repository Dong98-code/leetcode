/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} src1
 * @param {number} src2
 * @param {number} dest
 * @return {number}
 */
// 优先队列
import {
    PriorityQueue,
    MinPriorityQueue,
    MaxPriorityQueue,
    PriorityQueueOptions, // queue options interface
    PriorityQueueItem // queue item interface for min/max queue
} from '@datastructures-js/priority-queue';

// const {
//     PriorityQueue,
//     MinPriorityQueue,
//     MaxPriorityQueue
// } = require('@datastructures-js/priority-queue');
// class PriorityQueue {
//     constructor(
//         compare = (a, b) => a > b
//     ) {
//         this.data = []
//         this.size = 0
//         this.compare = compare
//     }

//     peek() {
//         return this.size === 0 ? null : this.data[0]
//     }

//     push(val) {
//         this.data.push(val)
//         // this._shifUp(this.size++)
//         this._shifUp(this.size);
//         this.size += 1;
//     }

//     pop() {
//         if (this.size === 0) {
//             return null
//         }
//         this._swap(0, --this.size)
//         this._shifDown(0)
//         return this.data.pop()
//     }

//     _parent(index) {
//         return index - 1 >> 1
//     }

//     _child(index) {
//         return (index << 1) + 1
//     }

//     _shifDown(index) {
//         while (this._child(index) < this.size) {
//             let child = this._child(index)
//             if (child + 1 < this.size &&
//                 this.compare(this.data[child + 1], this.data[child])) {
//                 child = child + 1
//             }
//             if (this.compare(this.data[index], this.data[child])) {
//                 break
//             }
//             this._swap(index, child)
//             index = child
//         }
//     }

//     _shifUp(index) {
//         while (this._parent(index) >= 0 &&
//             this.compare(this.data[index], this.data[this._parent(index)])) {
//             this._swap(index, this._parent(index))
//             index = this._parent(index)
//         }
//     }

//     _swap(a, b) {
//         [this.data[a], this.data[b]] = [this.data[b], this.data[a]]
//     }
// }
// var minimumWeight = function (n, edges, src1, src2, dest) {
//     function createGraph(edges) {
//         const g = {};
//         for (let [u, v, w] of edges) {
//             g[u] = g[u] || [];
//             g[u].push([v, w]);
//         }
//         return g;
//     }

//     function dijkstra(N, G, s) {
//         // 节点数目， 图， 源点
//         const dis = new Array(N).fill(Infinity);
//         dis[s] = 0;
//         const pq = new PriorityQueue((a, b) => a[1] > b[1]);
//         pq.push([s, 0]);
//         while (pq.size) {
//             const [f, d] = pq.pop()
//             if (d > dis[f] || !G[f]) {
//                 continue
//             }
//             for (const [t, w] of G[f]) {
//                 if (d + w < dis[t]) {
//                     dis[t] = d + w
//                     pq.push([t, dis[t]])
//                 }
//             }
//         }
//         return dis;
//     }

//     const g = createGraph(edges)
//     const rev = createGraph(edges.map(([f, t, w]) => [t, f, w]))
//     const da = dijkstra(n, g, src1)
//     const db = dijkstra(n, g, src2)
//     const dt = dijkstra(n, rev, dest)
//     let ans = Infinity
//     // 枚举 src1 src2 dest 最短路的交点
//     for (let i = 0; i < n; i++) {
//         ans = Math.min(ans, da[i] + db[i] + dt[i])
//     }
//     return ans === Infinity ? -1 : ans
// };
var minimumWeight = function (n, edges, src1, src2, dest) {
    //leetcode自带 优先级队列
    function createGraph(edges) {
        const g = {};
        for (let [u, v, w] of edges) {
            g[u] = g[u] || [];
            g[u].push([v, w]); // 第一个值为目标节点， 第二个值为距离

        }
        return g;
    }

    function dijkstra(N, G, s) {
        const dis = new Array(N).fill(Infinity);
        dis[s] = 0;
        // 初始化一个最小堆
        const pq = new MinPriorityQueue({
            priority: (item) => item[1]
        }); // 使用自定的PQ 需要指定优先级
        pq.enqueue([s, 0]);
        while (!pq.isEmpty()) { // 非空的时候执行
            const [f, d] = pq.dequeue().element;
            if (d > dis[f] || !G[f]) {
                continue;
            }
            for (const [t, w] of G[f]) {
                if (d + w > dis[t]) {
                    dis[t] = d + w; // 更新最短距离
                    pq.enqueue([t, dis[t]]);
                }
            }
        }
        return dis;
    }

    const g = createGraph(edges)
    const rev = createGraph(edges.map(([f, t, w]) => [t, f, w]))
    const da = dijkstra(n, g, src1)
    const db = dijkstra(n, g, src2)
    const dt = dijkstra(n, rev, dest)
    let ans = Infinity
    // 枚举 src1 src2 dest 最短路的交点
    for (let i = 0; i < n; i++) {
        ans = Math.min(ans, da[i] + db[i] + dt[i])
    }
    return ans === Infinity ? -1 : ans
};
n = 6
edges = [
    [0, 2, 2],
    [0, 5, 6],
    [1, 0, 3],
    [1, 4, 5],
    [2, 1, 1],
    [2, 3, 3],
    [2, 3, 4],
    [3, 4, 2],
    [4, 5, 1]
]
src1 = 0
src2 = 1
dest = 5
console.log(minimumWeight(n = n, edges = edges, src1 = src1, src2 = src2, dest = dest));
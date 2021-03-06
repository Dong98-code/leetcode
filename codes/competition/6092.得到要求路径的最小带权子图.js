/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} src1
 * @param {number} src2
 * @param {number} dest
 * @return {number}
 */
// δΌειε
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
//         // θηΉζ°η?οΌ εΎοΌ ζΊηΉ
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
//     // ζδΈΎ src1 src2 dest ζη­θ·―ηδΊ€ηΉ
//     for (let i = 0; i < n; i++) {
//         ans = Math.min(ans, da[i] + db[i] + dt[i])
//     }
//     return ans === Infinity ? -1 : ans
// };
var minimumWeight = function (n, edges, src1, src2, dest) {
    //leetcodeθͺεΈ¦ δΌεηΊ§ιε
    function createGraph(edges) {
        const g = {};
        for (let [u, v, w] of edges) {
            g[u] = g[u] || [];
            g[u].push([v, w]); // η¬¬δΈδΈͺεΌδΈΊη?ζ θηΉοΌ η¬¬δΊδΈͺεΌδΈΊθ·η¦»

        }
        return g;
    }

    function dijkstra(N, G, s) {
        const dis = new Array(N).fill(Infinity);
        dis[s] = 0;
        // εε§εδΈδΈͺζε°ε 
        const pq = new MinPriorityQueue({
            priority: (item) => item[1]
        }); // δ½Ώη¨θͺε?ηPQ ιθ¦ζε?δΌεηΊ§
        pq.enqueue([s, 0]);
        while (!pq.isEmpty()) { // ιη©ΊηζΆεζ§θ‘
            const [f, d] = pq.dequeue().element;
            if (d > dis[f] || !G[f]) {
                continue;
            }
            for (const [t, w] of G[f]) {
                if (d + w > dis[t]) {
                    dis[t] = d + w; // ζ΄ζ°ζη­θ·η¦»
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
    // ζδΈΎ src1 src2 dest ζη­θ·―ηδΊ€ηΉ
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
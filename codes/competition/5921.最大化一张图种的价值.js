/**
 * @param {number[]} values
 * @param {number[][]} edges
 * @param {number} maxTime
 * @return {number}
 */
 var maximalPathQuality = function(values, edges, maxTime) {
    let n = values.length;
    let graph = {};
    for (let e of edges) {
        graph[e[0]] = graph[e[0]] || [];
        graph[e[0]].push([e[1],e[2]]);
        graph[e[1]] = graph[e[1]] || [];
        graph[e[1]].push([e[0],e[2]]);
    }
    if (!graph[0]) {
        return values[0];
    }
    let res = values[0];
    let q = [];
    q.push([0, values[0], maxTime, 1]);
    while (q.length !== 0) {
        let item = q.shift();
        let cur = item[0], v = item[1], t = item[2], path=item[3];
        if (cur == 0) {
            res = Math.max(res, v);  // 更新价值最大值
        }
        for (let item_2 of graph[cur]) {
            let next = item_2[0];
            let time = item_2[1];
            if (t >= time) {
                if (path & 1 << next) {
                    q.push([next, v, t-time, path]);
                } else {
                    q.push([next, v+values[next], t-time, path | 1 << next]);
                }
            }
        }
    }
    return res;
};
values = [0, 32, 10, 43];
edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]];
maxTime = 49;
console.log(maximalPathQuality(values, edges, maxTime));
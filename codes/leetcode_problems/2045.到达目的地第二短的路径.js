/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} time
 * @param {number} change
 * @return {number}
 */
 var secondMinimum = function(n, edges, time, change) {
    // 第一步 建图
    let graph = new Array(n+1);
    let dis = new Array(n+1);
    for (let i=0;i<=n;i++) {
        graph[i] = [];
        dis[i] = [Number.MAX_VALUE, Number.MAX_VALUE]; // 初始化
    }
    dis[1][0] = 0;
    for (let edge of edges) {
        
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    }
    // 
    let q = [];
    
    q.push([1, 0])  // [node, dis]
    while (dis[n][1] === Number.MAX_VALUE) {
        let [x, d] = q.shift(); 
        for (let y of graph[x]) {
            if (d+1 < dis[y][0]) {
                dis[y][0] = d+1;
                q.push([y, d+1]);
            } else if (d+1 > dis[y][0] && d+1 < dis[y][1])  {
                dis[y][1] = d+1;
                q.push([y, d+1]);
            }
        }

    }
    let res = 0;
    for (let i=0;i<dis[n][1];i++) {
        if (res % (2*change) >= change) {
            res = res + (2*change - res % (2*change)); 
        }
        res = res + time;
    }
    
    return res;
};
n = 5, edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time = 3, change = 5
console.log(secondMinimum(n, edges, time, change))
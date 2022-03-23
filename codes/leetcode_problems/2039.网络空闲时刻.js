var networkBecomesIdle = function(edges, patience) {
    // 权值均为1 先访问到它 即可得到最短路径
    let q = [];
    q.push(0)
    let ans = 0, dis = 1;
    let n = patience.length;
    let vis = new Array(n).fill(0);
    vis[0] = 1;
    // 建图
    let graph = new Array(n).fill(0).map(ele => []);
    for (let [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }
    while (q.length !== 0) {
        let l = q.length;
        for (let i=0; i < l;i++) {
            const u = q.shift();
            for (let v of graph[u]) {
                if (vis[v]) {
                    continue;
                }
                vis[v] = 1;
                // 计算时间
                q.push(v);
                const cnt = Math.ceil(dis * 2 / patience[v]);
                const time = (cnt - 1) * patience[v] + 2 * dis + 1;
                ans = Math.max(time, ans);
            }
        }
        dis += 1;
    }
    return ans;
};

console.log(networkBecomesIdle(edges=[[0,1],[1,2]], patience=[0, 2, 1]));
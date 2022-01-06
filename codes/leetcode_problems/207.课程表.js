/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
 var canFinish = function(numCourses, prerequisites) {
     let graph = new Array(numCourses);
     for (let i = 0; i < numCourses; i++) {
         graph[i] = [];
     }
    let inDegree = new Array(numCourses).fill(0);
    for (let pre of prerequisites) {
        let u = pre[0], v = pre[1];
        graph[v].push(u);  // tail:v -> head:u
        inDegree[u] += 1;  // 对应的入度 + =1
    }
    let q = new Array();
    for (let i=0;i<numCourses;i++) {
        if (inDegree[i] == 0) {
            q.push(i);  // 将入度为0的节点加入到 队列中
        }
    }
    let cnt = 0;
    while (q.length !== 0) {
        let tail = q.shift();
        cnt += 1;
        for (let head of graph[tail]) {
            inDegree[head] -= 1;
            if (inDegree[head] == 0) {
                q.push(head)
            }
        }

    }
    return cnt == numCourses;
};
console.log(canFinish(2, [[1,0]]))
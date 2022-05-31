var pacificAtlantic = function(heights) {
    // 只有两个点能流向大西洋和太平洋
    // bfs 第一次边界， 第二次
    let m = heights.length;
    let n = heights[0].length;
    let P = new Array(m).fill(0).map(el => {
        return new Array(n).fill(false);
    })
    let A = new Array(m).fill(0).map(el => {
        return new Array(n).fill(false);
    });
    let directions = [[-1,0], [1, 0], [0,1], [0,-1]];
    const bfs = function(row, col, array) {
        if (array[row][col]) return;
        let q = [];
        q.push([row, col]);
        // 开始搜索
        array[row][col] = true;
        while (q.length >0 ) {
            let [x, y] = q.shift();
            for (let [dx, dy] of directions) {
                let new_x = x + dx;
                let new_y = y + dy;
                if (new_x >= 0 && new_x < m && new_y >= 0 && new_y < n && heights[x][y] <= heights[new_x][new_y] && !(array[new_x][new_y])) {
                    array[new_x][new_y] = true;
                    q.push([new_x, new_y]);
                }
            }
        }
    }
    for (let i = 0, j=0; j<n;j++) {
        bfs(i, j, P);
    }
    for(let i=0,j=0;i< m;i++) {
        bfs(i, j, P);
    }

    for (let i=m-1, j=0;j<n;j++) {
        bfs(i,j,A);

    }
    for (let i=0,j=n-1;i<m;i++) {
        bfs(i, j, A);
    }

    let res = [];
    for (let i = 0; i<m;i++) {
        for (let j=0;j<n;j++) {
            if (P[i][j] && A[i][j]) {
                res.push([i, j]);
            }
        }
    }
    return res;
};

let heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]];
console.log(pacificAtlantic(heights));
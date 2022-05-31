var findRightInterval = function(intervals) {
    let n = intervals.length;
    let s = new Array(n).fill(0).map(() => new Array(2).fill(0));
    let e = new Array(n).fill(0).map(() => new Array(2).fill(0));

    for (let i = 0; i< n; i++) {
        s[i][0] = intervals[i][0];
        s[i][1] = i;
        e[i][0] = intervals[i][1];
        e[i][1] = i;

    }

    s.sort((a, b) => a[0]-b[0]);
    e.sort((a, b) => a[0] - b[0]);

    // let i = 0, j = 0;
    let ans = new Array(n).fill(0);
    for (let i = 0, j=0; i<n;i++) {
        while(j < n && e[i][0] > s[j][0]) {
            j++;
        }
        if (j < n) {
            ans[e[i][1]] = s[j][1];
        } else {
            ans[e[i][1]] = -1;
        }
    }
    return ans;

};

console.log(findRightInterval([[3,4],[2,3],[1,2]]))
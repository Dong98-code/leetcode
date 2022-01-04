/**
 * @param {number[]} changed
 * @return {number[]}
 */
 var findOriginalArray = function(changed) {
    changed.sort((a, b)=>a-b);  // 升序排列
    let l = 0, r = 1;
    let n = changed.length;
    let ans = new Array();
    if (n % 2 == 1) {
        return [];
    }
    let visited = new Array(n).fill(false);  // 设置已经访问过的值
    for (let i=0;i<Math.floor(n/2);i++) {
        while (visited[l]) {
            l += 1;
        }
        if (l == r) {
            r = l + 1;
        }
        while (r < n && changed[r] !== changed[l]*2) {
            r += 1;
        }
        if (r == n) {
            return [];  // 此时该原数组不存在
        }
        visited[r] = true;  // 此时 r处的数字已经访问过
        ans.push(changed[l]);
        l += 1;
        r += 1;

    }
    if (ans.length*2 == n) {
        return ans;
    }
    return [];
    
};

console.log(findOriginalArray([1,3,4,2,6,8]))

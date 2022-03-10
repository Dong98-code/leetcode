/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
//  class UnionFind {
//     constructor(n) {
//         this.parent = new Array(n).fill(0).map((element, index) => index);
//         // 初始化 parent
//     }

//     find(x) {
//         while (x !== this.parent[x]) {
//             this.parent[x] = this.find(this.parent[x]);
//             x = this.parent[x];

//         }
//         return x;
//     }
//     union(x, y) {
//         const root_x = this.find(x), root_y = this.find(y);
//         if (root_x !== root_y) {
//             this.parent[root_x] = root_y;
//             return true; 
//         }
//         return false;
//     }


//  }
// var findAllPeople = function(n, meetings, firstPerson) {
//     meetings.sort((a, b)=> a[2] - b[2]);
//     let res = [];
//     let uf = new UnionFind(n);
//     uf.union(firstPerson, 0);

//     let m = meetings.length;
//     let i = 0;
//     while (i < m) {
//         let j = i+1;
//         while (j < m && meetings[j][2] == meetings[i][2]) {

//             j += 1;
//         }
//         for (let k = i; k < j; k++) {
//             let p1 = meetings[k][1], p2 = meetings[k][0];
//             uf.union(p1, p2);
//         }
//         const init = uf.find(0);
//         for (let k=i; k<j;k++) {
//             let p1 = meetings[k][1], p2 = meetings[k][0];
//             if (uf.find(p1) !== init) {uf.parent[p1] = p1}
//             if (uf.find(p2) !== init) {uf.parent[p2] = p2}
//         }
//         i = j;

//     }
//     const init = uf.find(0);
//     for (let i=0;i<n;i++) {
//         if(uf.find(i) === init) res.push(i);
//     }
//     return res;
// };

var findAllPeople = function (n, meetings, firstPerson) {
    // 查找每个元素的祖先节点
    function find(x){
        if(p[x] != x) {
            p[x] = find(p[x])
        }
        return p[x];

    }
    let p = new Array(n).fill(1).map((elsement, index) => index);
    meetings.sort((a, b)=> a[2] - b[2]); // 按照时间升序排列
    
    let m = meetings.length;
    p[firstPerson] = 0;
    let i = 0;
    while (i < m) {
        let j = i + 1;
        while (j < m && meetings[j][2] == meetings[i][2]) {
            j += 1;
        }
        // 第一此遍历
        for (let k = i; k < j;k++) {
            // 以 0 为目标根节点
            // 如果任意一个节点的根节点为0 则把他们的的根节点都变成0
            //注意此时如果a，b是某个节点的子节点，此时只是将它们父节点（因为路径压缩所以是父节点）的根节点更新为0，而不是将它们的父节点更新为0
            let [a, b] = [meetings[k][0], meetings[k][1]];
            if(p[find(a)] == 0 || p[find(b)] == 0) {// 祖先节点的祖先节点
                p[find(a)] = 0;
                p[find[b]] = 0;
            }
            p[find(a)] = p[find(b)]; // 把一个节点的根节点 变成另外一个的根节点
        }
        // 第二次遍历
        for (let k = i; k< j;k++) {
            //路径压缩，将a和b和中途的节点全部直接连接上根节点，处理第一次遍历后没有直接连上根节点的情况
            //  //如果路径压缩后，父节点（路径压缩后即根节点）仍然不是0，将它们初始化以待下次使用
            // const init = find(0)
            let [a, b] = [meetings[k][0], meetings[k][1]];
            if(p[find(a)] == 0 || p[find(b)] == 0) {// 祖先节点的祖先节点
                p[find(a)] = 0;
                p[find[b]] = 0;
            } else {
                p[a] = a;
                p[b] = b;
            }
        }
        i = j;
    }
    
    let res = [];
    for (let i=0;i<n;i++) {
        if (p[find(i)] == 0) {
            res.push(i);
        }
    }
    return res;
};
console.log(findAllPeople(n = 6, meetings = [
    [2, 1, 1],
    [0, 1, 1],
    [3, 2, 1],
    [4, 2, 2]
], firstPerson = 5));
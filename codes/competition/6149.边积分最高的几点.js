var edgeScore = function(edges) {
    let cnt = new Map();
    for (let [index, value] of edges.entries()) {
        if (!cnt.get(value)) {
            cnt.set(value, index);
        } else {
            cnt.set(value, index + cnt.get(value));
        }
    }
    let res_sum = 0;
    let res = 0;
    let index = [...cnt.keys()];
    index.sort((a, b) => b - a); // 降序排列
    for (let i of index) {
        if (cnt.get(i) >= res_sum) {
            res = i;
            res_sum = cnt.get(i)
        }
    }
    return res;
};
console.log(edgeScore([2, 0, 0,2]));
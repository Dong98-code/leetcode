var groupThePeople = function(groupSizes) {
    let cnt_map = new Map();
    for (let [index, item] of groupSizes.entries()) {
        if (!cnt_map.get(item)) {
            //空
            cnt_map.set(item, {"cur":1, "arr":[[index]]}) // cur当前 人数; 数组形式
        } else {
            // 
            let tem = cnt_map.get(item);
            let cur = tem.cur += 1;
            let arr = tem.arr;
            if (Math.ceil(cur/item) > arr.length) {
                // 新增一个
                arr.push([index])
            } else {
                arr[arr.length-1].push(index);
            }
            cnt_map.set(item, {cur, arr}) // 更新map
        }
    }
    let res = [];
    //遍历map;
    for (let [k,v] of cnt_map) {
        res = res.concat(v.arr)
    }
    return res;
};
console.log(groupThePeople([3,3,3,3,3,1,3]));
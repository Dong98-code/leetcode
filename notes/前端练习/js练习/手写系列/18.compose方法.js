var list = [['热', '冷', '冰'], ['大', '中', '小'], ['重辣', '微辣'], ['重麻', '微麻']];

// // 输出所有维度的组合，如 [['热', '冷''], ['大', '中']]  => 热+大，热+中，冷+大，冷+中

// function compose(list) {
//   console.log('hello world');
// }

// compose(list);

function compose(list){
    // for循环
    let res = [];
    if (!list.length) return [];
    for (let subList of list) {
        // 第一次
        if (res.length === 0) {
            res = subList.map(item => [item]);
        } else {
            // 之后的次数
            let subRes = [];
            for (let r of res) {
                let tailList = subList.map(item => [...r, item]);
                subRes.push(...tailList) //
            }
            res = subRes
        }
    }
    return res.map(arr => arr.join("+"));
}

let res = compose(list);
console.log(res);

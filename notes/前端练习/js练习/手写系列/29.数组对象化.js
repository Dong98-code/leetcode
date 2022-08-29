const input = {
    'a.b.c': 1,
    'a.b.d': 2,
    'a.e': 3,
    'f': 4,
};
const output = {
    a: {
        b: {
            c: 1,
            d: 2
        },
        e: 3
    },
    f: 4
};

const reversFlatten = function (obj) {
    const keys = Object.keys(obj);//可迭代的 自身的 不包含symbol
    const res = {};
    for (let key of keys) {
        //遍历属性值
        let chain = key.split(".");//["a","b"]
        let tmp = res;
        for (let i = 0; i < chain.length; i++) {
            let k = chain[i];// "a"
            // if (tmp[k] !== undefined) {
            //     tmp[k] = tmp[k]; // 不做修改
            // } else {
            //     // 此时tmp[k]为空
            //     tmp[k] = i === chain.length - 1 ? obj[key] : {}
            // }
            tmp[k] = tmp[k] ?? (i === chain.length - 1 ? obj[key] : {})
            tmp = tmp[k];//tmp指向新的创建的对象
        }
        
    }
    return res;
}

console.log(reversFlatten(input));
// 博客参考 https://juejin.cn/post/6844903929705136141 深拷贝和浅拷贝
//#region 
// function clone(target) {
//     let clone_target = {};
//     for (const key in target) {
//         clone_target[key] = target[key];
//     }
//     return clone_target;
// }
//#endregion
// 深拷贝
const target = {
    field1: 1,
    field2: undefined,
    field3: 'ConardLi',
    field4: {
        child: 'child',
        child2: {
            child2: 'child2'
        }
    }
};
// target仅仅为对象
function deepCloneV1(target) {
    if (typeof target === 'object') {
        let clone_target = {};
        for (const key in target) {
            clone_target[key] = deepCloneV1(target[key]);
        }
        return clone_target;
    } else {
        return target;
    }
}
// const clone_target = deepCloneV1(target)
// console.log(clone_target); 

function deepCloneV2(target) {
    // 深拷贝数组和对象
    if (typeof target === 'object') {
        let clone_target = Array.isArray(target) ? [] : {};
        for (const key in target) {
            clone_target[key] = deepCloneV2(target[key]);

        }
        return clone_target;
    } else {//原始数据类型 直接返回
        return target;
    }
}

const target2 = {
    field1: 1,
    field2: undefined,
    field3: {
        child: 'child'
    },
    field4: [2, 4, 8]
};

// const clone_target2 = deepCloneV2(target2);
// console.log(clone_target2);

// v3: 循环引用的情况；
function deepCloneV3(target, map=new Map()) {
    if (typeof target === "object") {
        let clone_target = Array.isArray(target) ? [] : {};
        if (map.get(target)) {
            return map.get(target);
        }
        map.set(target, clone_target); // 原始的target和clone——target建立映射
        for (const key in target) {
            clone_target[key] = deepCloneV3(target);
        }
        return clone_target;
    } else {
        return target;
    }
}


// v3 性能优化，自定义forEach函数
a = [1, 2]
b = {1:2, 2:2}
console.log(b || a)
function forEach(array, iteratee) {// iteratee回调函数
    let index = -1;
    const length = array.length;
    while (++index < length) {// ++idx先判断再自增1
        iteratee(array[index], index);// 执行该回调函数
    }
    return array;
}

function deepCloneV4(target, map = new WeakMap()) {// weekMap 弱引用类型， 垃圾回收
    if (typeof target === 'object') {
        const isArray = Array.isArray(target);// 用于判断是否为 数组
        let cloneTarget = isArray ? [] : {};

        if (map.get(target)) {
            return map.get(target);
        }
        map.set(target, cloneTarget);

        const keys = isArray ? undefined : Object.keys(target); // 如果是数组
        forEach(keys || target, (value, key) => {
            if (keys) {// 此时为onject
                key = value;// value为keys中值
            }
            // 此时 target为 数组， key为target的索引值
            cloneTarget[key] = deepCloneV4(target[key], map);
        });

        return cloneTarget;
    } else {
        return target;
    }
}

function deepCloneV5(obj, map = new WeakMap()) {
    if (obj === null) return obj; // null直接返回
    if (obj instanceof Date) return new Date(obj);
    // 判断是不是对象 {}
    if (typeof obj !== "object") {
        return obj;
    }
    // 是对象 进行循环递归 ，注意循环引用
    if (map.has(obj)) {
        return map.get(obj);
    }
    let cloneObj = new obj.constructor();
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloneObj[key] = deepCloneV5(obj[key], map)
        }
    }
    return cloneObj;
}

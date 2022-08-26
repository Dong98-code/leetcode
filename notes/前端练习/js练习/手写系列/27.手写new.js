function myNew(Fn, ...arg) {
    let res = {}; // 1. 新建空对象
    if (Fn.prototype !== null) {
        Object.setPrototypeOf(res, Fn.prototype); // 对象的 __proto__指向够高函数
    }
    let returRes = Fn.apply(res, arg);
    if ((typeof returRes === 'object' || typeof returRes === 'function') && returRes !== null) {
        return returRes;
    }
    return res;
};
Promise.all = function (promises) {
    // promises 类数组形式
    if (typeof promises[Symbol.iterator] !== 'function') {
        reject("Type error");
    }

    if (promises.length === 0) {
        resolve([]);
    } else {
        const res = [];
        let count = 0;
        const len = promises.length;
        for (leti = 0; i < len; i++) {
            // 可能为thenable对象，直接调用then
            Promise.resolve(promises[i]).then(data => {
                res[i] = data;
                if (++count === len) {
                    resolve(res);
                }
            }).catch(err => {
                reject(err);
            })
        }
    }


}
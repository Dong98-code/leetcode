const isFunction = function (fun) {
    return typeof fun === 'function';
};
const isObject = function (value) {
    return value !== null && typeof value === 'object';
};


class MyPromise {
    static PENDING = "pending";
    static FULFILLED = 'fulfilled';
    static REJECTED = "rejected";

    constructor(handle) {
        if (!isFunction(handle)) {
            throw new Error('MyPromise resolver is not a function'); //构造函数传入参数必须是一个函数
        }
        this.PromiseState = MyPromise.PENDING; // 状态属性，初始值为pending
        this.PromiseResult = null; // 结果初始值为null
        this.onFulfilledCallbacks = []; //保存成功的回调函数
        this.onRejectedCallbacks = []; //失败的回调函数
        try {
            // 同步执行handle
            handle(this._resolve.bind(this), this._reject.bind(this))
        } catch (err) {
            this._reject(err); // 生成实例时， 报错 把错误信息返回reject方法， 执行reject
        }
    }


    _resolve(result) {
        // console.log("resolve");
        if (this.PromiseState !== MyPromise.PENDING) {
            return;
        }
        const resolveHandle = (result) => {
            this.PromiseState = MyPromise.FULFILLED;
            this.PromiseResult = result;
            // this.onFulfilledCallbacks.forEach(callback => {
            //     callback(result)
            // })
            while (this.onFulfilledCallbacks.length) {
                const cb = this.onFulfilledCallbacks.shift();
                cb(result);
            }
        }
        const rejectHandle = reason => {
            this.PromiseState = MyPromise.REJECTED;
            this.PromiseResult = reason;
            // this.onRejectedCallbacks.forEach(callback => {
            //     callback(reason)
            // })
            while (this.onRejectedCallbacks.length) {
                const cb = this.onRejectedCallbacks.shift();
                cb(reason);
            }
        }

        if (result instanceof MyPromise) {
            if (result === this) {
                return rejectHandle(new TypeError(''));
            }
            result.then(resolveHandle, rejectHandle);
        } else {
            // 执行_fulfilledQueue中的任务
            // 所有 onFulfilled 需按照其注册顺序依次回调
            resolveHandle(result);
        }
    }

    _reject(reason) {
        if (this.PromiseState !== MyPromise.PENDING) {
            return;
        }
        this.PromiseState = MyPromise.REJECTED;
        this.PromiseResult = reason;
        // this.onRejectedCallbacks.forEach(callback => {
        //     callback(reason)
        // })
        while (this.onRejectedCallbacks.length) {
            const cb = this.onRejectedCallbacks.shift();
            cb(reason);
        }
    }

    then(onFulfilled, onRejected) {
        // 首先判断 两个回调函数是否为函数，如果不为函数 忽略：
        // 1. onFulfiled 原封不动返回 value
        //2. 返回 reason throw  a erroe


        //返回的是一个全新的promise
        let promise2 = new MyPromise((resolve2, reject2) => {
            // .then为微任务 所以返回的时候应该 使用异步
            const fulfilledHandle = (result) => {
                queueMicrotask(() => {
                    if (!isFunction(onFulfilled)) {
                        resolve2(result);
                    } else {
                        try {
                            const res = onFulfilled(result);
                            resolvePromise(promise2, res, resolve2, reject2)
                        } catch (e) {
                            reject2(e);
                        }
                    }
                });

            }
            const rejectedHandle = (reason) => {
                queueMicrotask(() => {
                    if (!isFunction(onRejected)) {
                        reject2(reason)
                    } else {
                        try {
                            const res = onRejected(reason);
                            resolvePromise(promise2, res, resolve2, reject2)
                        } catch (e) {
                            reject2(e)
                        }
                    }
                })
            }
            switch (this.PromiseState) {
                case MyPromise.PENDING:
                    this.onFulfilledCallbacks.push(fulfilledHandle)
                    this.onRejectedCallbacks.push(rejectedHandle);
                    break;
                case MyPromise.FULFILLED:
                    fulfilledHandle(this.PromiseResult);
                    break;
                case MyPromise.REJECTED:
                    rejectedHandle(this.PromiseResult);
                    break;
                default:
            }

        })

        return promise2;
    }

    static resolve(value) {
        // MyPromise.resolve()
        // 1.如果输入的value为普通值， reslove(x)
        // promise 返回promise
        // .then() 返回的promise会跟随这个thenable对象
        if (value instanceof MyPromise) {
            return value; //直接返回
        } else if (value instanceof Object && "then" in value) {
            try {
                var then = value.then;
                if (isFunction(then)) {
                    return new MyPromise(then.bind(value));
                }
            } catch (e) {
                return new MyPromise((reslove, reject) => {
                    reject(e);
                })
            }


        }
        return new MyPromise((resolve) => {
            resolve(value)
        })
    }

    static reject(reason) {
        return new MyPromise((resolve, reject) => {
            reject(reason);
        })
    }

    catch (onRejected) {
        // onRejected 抛出一个错误或者返回一个失败的promise 返回一个失败的promise
        return this.then(undefined, onRejected)
    } finally(callback) {
        // 无论结果如何都会执行
        // 调用then 无论成功失败都会调用一次 callback
        return this.then(callback, callback);
    }

    static all(promiseList) {
        // 传入的是一个可迭代的对象 有interator接口
        return new MyPromise((resolve, reject) => {
            let list;
            try {
                list = [...promiseList] //只解析第一层
            } catch (e) {
                reject(new TypeError(`${promiseList} is not iterable (cannot read property Symbol(Symbol.iterator))`))
                return;
            }
            let len = list.length; //长度
            if (len === 0) {
                //空数组
                resolve([]); //当且仅当传入的数组为空时 为同步代码执行，之后的异步代码；.then（）微任务
            }

            let fulfilledCount = 0; //用于记录完成的promise
            let res = []; //存储结果的
            for (let [i, p] of list.entries()) {
                //索引和对应的值
                MyPromise.resolve(p)
                    .then((result) => {
                        res[i] = result;
                        fulfilledCount += 1;
                        if (fulfilledCount === len) {
                            resolve(res);
                        }
                    }, (err) => {
                        reject(err);
                    })
            }
        })
    }

    static allSettled(promiseList) {
        return new MyPromise((resolve, reject) => {
            let list;
            try {
                list = [...promiseList] //只解析第一层
            } catch (e) {
                reject(new TypeError(`${promiseList} is not iterable (cannot read property Symbol(Symbol.iterator))`))
                return;
            }



            let unsettledCount = list.length;
            if (unsettledCount === 0) {
                //空数组
                resolve([]); //当且仅当传入的数组为空时 为同步代码执行，之后的异步代码；.then（）微任务
            }
            let res = [];
            for (let [i, p] of list.entries()) {
                MyPromise.resolve(p).then((result) => {
                    res[i] = {
                        status: 'fulfilled',
                        value: result
                    };


                }, (reason) => {
                    res[i] = {
                        status: "rejected",
                        reason: reason
                    }
                }).finally(() => {
                    unsettledCount--;
                    if (unsettledCount === 0) {
                        resolve(res)
                    }
                });
            }
        })
    }

    static any(promiseList) {
        return new MyPromise((resolve, reject) => {
            let list;
            try {
                list = [...promiseList]
            } catch (err) {
                reject(new TypeError(`${promiseList} is not iterable (cannot read property Symbol(Symbol.iterator))`))
            }

            let len = list.length;
            let errors = [];
            if (len === 0) {
                //没有成功的
                reject(new AggregateErroe(errors, 'all promises were rejected'))
            }

            let rejectedCount = 0;
            for (let [i, p] of list.entries()) {
                MyPromise.resolve(p).then(
                    (result) => {
                        resolve(result)
                    },
                    (reason) => {
                        errors[i] = reason;
                        rejectedCount += 1;
                        if (rejectedCount === len) {
                            reject(new AggregateError(errors, 'All promises were rejected'));
                        }
                    }
                )
            }
        })
    }

    static race(promiseList) {
        return new MyPromise((resolve, reject) => {
            let list;
            try {
                list = [...promiseList];   
            } catch(err) {
                reject(new TypeError(`${promiseList} is not iterable (cannot read property Symbol(Symbol.iterator))`));
                return;
            }
            // 如果是空的永远是pending状态
            for (const p of list) {
                MyPromise.resolve(p).then(
                    (value) => {resolve(value) },
                    (reason) => {reject(reason)}
                )
            }
        })
    }
}


/**
 * 对resolve()、reject() 进行改造增强 针对resolve()和reject()中不同值情况 进行处理
 * @param  {promise} promise2 promise1.then方法返回的新的promise对象
 * @param  {[type]} x         promise1中onFulfilled或onRejected的返回值
 * @param  {[type]} resolve   promise2的resolve方法
 * @param  {[type]} reject    promise2的reject方法
 */

function resolvePromise(promise2, x, resolve, reject) {
    // 2.3.1 promise x指向同一对象， 以typeErroe 拒绝promis
    if (promise2 === x) {
        return reject(new TypeError('Chaning cycle detected for promise'))
    }

    // 2.3.2 如果x为promis 则promise2接受 x的状态
    if (x instanceof MyPromise) {
        x.then(y => {
            // x的状态改变， 返回 y
            resolvePromise(promise2, y, resolve, reject);
        }, reject)
        return;
    }
    if (isFunction(x) || isObject(x)) {
        //x为对象或者函数
        // 2.3.3.1 把x.then 赋值给then
        try {
            var then = x.then;
        } catch (e) {
            reject(e) //x.then的时候抛出错误
        }

        if (isFunction(then)) {
            // 2.3.3.3 then为函数 把 x作为作用域this调用
            // 2.3.3.3.3 保留第一调用的记过
            let called = false;
            try {
                then.call(x, y => {
                    if (called) return;
                    called = true;
                    resolvePromise(promise2, y, resolve, reject);
                }, r => {
                    if (called) return;
                    called = true;
                    reject(r); //拒绝 r
                })
            } catch (e) {
                // 如果此时 已经 调用 called true 忽略
                if (called) return;
                called = true;
                reject(e);
            }
        } else {
            resolve(x);
        }
    } else {
        // x不为函数 或者对象 promise类型， 以x 为类型执行promise
        return resolve(x);
    }
}




MyPromise.deferred = function () {
    let result = {};
    result.promise = new MyPromise((resolve, reject) => {
        result.resolve = resolve;
        result.reject = reject;
    });
    return result;
}


// var promisesAplusTests = require("promises-aplus-tests");
// const {
//     reject
// } = require("underscore");

// promisesAplusTests(MyPromise, function (err) {
//     console.log(err);
//     // All done; output is in the console. Or check `err` for number of failures.
// });

/*
测试promise.all()*/

const pErr = new MyPromise((resolve, reject) => {
    reject("总是失败");
  });
  
  const pSlow = new MyPromise((resolve, reject) => {
    setTimeout(resolve, 500, "最终完成");
  });
  
  const pFast = new MyPromise((resolve, reject) => {
    setTimeout(resolve, 100, "很快完成");
  });
  
  MyPromise.any([pErr, pSlow, pFast]).then((value) => {
    console.log(value);
    // pFast fulfils first
  })
  // 期望输出: "很快完成"
  
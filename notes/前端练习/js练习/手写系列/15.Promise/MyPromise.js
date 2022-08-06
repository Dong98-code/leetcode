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
            handle(this.resolve.bind(this), this.reject.bind(this))
        } catch (err) {
            this.reject(err); // 生成实例时， 报错 把错误信息返回reject方法， 执行reject
        }
    }


    resolve(result) {
        // console.log("resolve");
        if (this.PromiseState === MyPromise.PENDING) {
            queueMicrotask(() => {
                this.PromiseState = MyPromise.FULFILLED;
                this.PromiseResult = result;
                this.onFulfilledCallbacks.forEach(callback => {
                    callback(result)
                })
            });
        }
    }

    reject(reason) {
        if (this.PromiseState === MyPromise.PENDING) {
            queueMicrotask(() => {
                this.PromiseState = MyPromise.REJECTED;
                this.PromiseResult = reason;
                this.onRejectedCallbacks.forEach(callback => {
                    callback(reason)
                })
            });

        }
    }

    // then(onFulfilled, onRejected) {
    //     onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : value => value;
    //     onRejected = typeof onRejected === 'function' ? onRejected : reason => {
    //         throw reason;
    //     };

    //     let promise2 = new MyPromise((resolve, reject) => {
    //         if (this.PromiseState === MyPromise.FULFILLED) {
    //             queueMicrotask(() => {
    //                 try {
    //                     let x = onFulfilled(this.PromiseResult);
    //                     resolvePromise(promise2, x, resolve, reject);
    //                 } catch (e) {
    //                     reject(e);
    //                 }
    //             });
    //         } else if (this.PromiseState === MyPromise.REJECTED) {
    //             queueMicrotask(() => {
    //                 try {
    //                     let x = onRejected(this.PromiseResult);
    //                     resolvePromise(promise2, x, resolve, reject);
    //                 } catch (e) {
    //                     reject(e)
    //                 }
    //             });
    //         } else if (this.PromiseState === MyPromise.PENDING) {
    //             this.onFulfilledCallbacks.push(() => {
    //                 try {
    //                     let x = onFulfilled(this.PromiseResult);
    //                     resolvePromise(promise2, x, resolve, reject)
    //                 } catch (e) {
    //                     reject(e);
    //                 }
    //             });
    //             this.onRejectedCallbacks.push(() => {
    //                 try {
    //                     let x = onRejected(this.PromiseResult);
    //                     resolvePromise(promise2, x, resolve, reject);
    //                 } catch (e) {
    //                     reject(e);
    //                 }
    //             });
    //         }
    //     })

    //     return promise2
    // }
    then(onFulfilled, onRejected) {
        // 首先判断 两个回调函数是否为函数，如果不为函数 忽略：
        // 1. onFulfiled 原封不动返回 value
        //2. 返回 reason throw  a erroe
        onFulfilled = isFunction(onFulfilled) ? onFulfilled : value => value;
        onRejected = isFunction(onRejected) ? onRejected : reason => {
            throw reason;
        }

        //返回的是一个全新的promise
        let promise2 = new MyPromise((resolve, reject) => {
            // .then为微任务 所以返回的时候应该 使用异步
            if (this.PromiseState === MyPromise.FULFILLED) {
                // 根据成功的回调的结果的返回的值 确定返回的额promise的状态
                queueMicrotask(() => {
                    try {
                        let x = onFulfilled(this.PromiseResult);
                        resolvePromise(promise2, x, resolve, reject)
                    } catch (e) {
                        reject(e)
                    }
                })
            } else if (this.PromiseState === MyPromise.REJECTED) {
                queueMicrotask(() => {
                    try {
                        let x = onRejected(this.PromiseResult);
                        resolvePromise(promise2, x, resolve, reject)
                    } catch (e) {
                        reject(e); // 执行抛出异常 捕获错误
                    }
                })

            } else if (this.PromiseState === MyPromise.PENDING) {
                //添加回调函数进入到
                this.onFulfilledCallbacks.push(() => {
                    try {
                        let x = onFulfilled(this.PromiseResult);
                        resolvePromise(promise2, x, resolve, reject)
                    } catch (e) {
                        reject(e);
                    }
                });
                this.onRejectedCallbacks.push(() => {
                    try {
                        let x = onRejected(this.PromiseResult);
                        resolvePromise(promise2, x, resolve, reject);
                    } catch (e) {
                        reject(e);
                    }
                });
            }
        })

        return promise2;
    }
}


/**
 * 对resolve()、reject() 进行改造增强 针对resolve()和reject()中不同值情况 进行处理
 * @param  {promise} promise2 promise1.then方法返回的新的promise对象
 * @param  {[type]} x         promise1中onFulfilled或onRejected的返回值
 * @param  {[type]} resolve   promise2的resolve方法
 * @param  {[type]} reject    promise2的reject方法
 */
// function resolvePromise(promise2, x, resolve, reject) {
//     // 2.3.1规范 如果 promise 和 x 指向同一对象，以 TypeError 为据因拒绝执行 promise
//     if (x === promise2) {
//         return reject(new TypeError('Chaining cycle detected for promise'));
//     }

//     // 2.3.2规范 如果 x 为 Promise ，则使 promise2 接受 x 的状态
//     if (x instanceof MyPromise) {
//         if (x.PromiseState === MyPromise.PENDING) {
//             /**
//              * 2.3.2.1 如果 x 处于等待态， promise 需保持为等待态直至 x 被执行或拒绝
//              *         注意"直至 x 被执行或拒绝"这句话，
//              *         这句话的意思是：x 被执行x，如果执行的时候拿到一个y，还要继续解析y
//              */
//             x.then(y => {
//                 resolvePromise(promise2, y, resolve, reject)
//             }, reject);
//         } else if (x.PromiseState === MyPromise.FULFILLED) {
//             // 2.3.2.2 如果 x 处于执行态，用相同的值执行 promise
//             resolve(x.PromiseResult);
//         } else if (x.PromiseState === MyPromise.REJECTED) {
//             // 2.3.2.3 如果 x 处于拒绝态，用相同的据因拒绝 promise
//             reject(x.PromiseResult);
//         }
//     } else if (x !== null && ((typeof x === 'object' || (typeof x === 'function')))) {
//         // 2.3.3 如果 x 为对象或函数
//         try {
//             // 2.3.3.1 把 x.then 赋值给 then
//             var then = x.then;
//         } catch (e) {
//             // 2.3.3.2 如果取 x.then 的值时抛出错误 e ，则以 e 为据因拒绝 promise
//             return reject(e);
//         }

//         /**
//          * 2.3.3.3 
//          * 如果 then 是函数，将 x 作为函数的作用域 this 调用之。
//          * 传递两个回调函数作为参数，
//          * 第一个参数叫做 `resolvePromise` ，第二个参数叫做 `rejectPromise`
//          */
//         if (typeof then === 'function') {
//             // 2.3.3.3.3 如果 resolvePromise 和 rejectPromise 均被调用，或者被同一参数调用了多次，则优先采用首次调用并忽略剩下的调用
//             let called = false; // 避免多次调用
//             try {
//                 then.call(
//                     x,
//                     // 2.3.3.3.1 如果 resolvePromise 以值 y 为参数被调用，则运行 [[Resolve]](promise, y)
//                     y => {
//                         if (called) return;
//                         called = true;
//                         resolvePromise(promise2, y, resolve, reject);
//                     },
//                     // 2.3.3.3.2 如果 rejectPromise 以据因 r 为参数被调用，则以据因 r 拒绝 promise
//                     r => {
//                         if (called) return;
//                         called = true;
//                         reject(r);
//                     }
//                 )
//             } catch (e) {
//                 /**
//                  * 2.3.3.3.4 如果调用 then 方法抛出了异常 e
//                  * 2.3.3.3.4.1 如果 resolvePromise 或 rejectPromise 已经被调用，则忽略之
//                  */
//                 if (called) return;
//                 called = true;

//                 /**
//                  * 2.3.3.3.4.2 否则以 e 为据因拒绝 promise
//                  */
//                 reject(e);
//             }
//         } else {
//             // 2.3.3.4 如果 then 不是函数，以 x 为参数执行 promise
//             resolve(x);
//         }
//     } else {
//         // 2.3.4 如果 x 不为对象或者函数，以 x 为参数执行 promise
//         return resolve(x);
//     }
// }

function resolvePromise(promise2, x, resolve, reject) {
    // 2.3.1 promise x指向同一对象， 以typeErroe 拒绝promis
    if (promise2 === x) {
        return reject(new TypeError('Chaning cycle detected for promise'))
    }

    // 2.3.2 如果x为promis 则promise2接受 x的状态
    if (x instanceof MyPromise) {
        if (x.PromiseState === MyPromise.PENDING) {
            // 如果 x为pending 状态 需要 promise保持等待状态 直至 x被执行或者聚聚
            x.then(y => {
                // x的状态改变， 返回 y
                resolvePromise(promise2, y, resolve, reject);
            }, reject)
        } else if (x.PromiseState === MyPromise.FULFILLED) {
            // 返回一个成功的promise 值为改promise的值
            resolve(x.PromiseResult)
        } else if (x.PromiseState === MyPromise.REJECTED) {
            reject(x.PromiseResult)
        }

    } else if (isFunction(x) || isObject(x)) {
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


module.exports = MyPromise;

// console.log(1)

// const promise = new MyPromise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(2)
//     })

// })

// promise.then(value => {
//     console.log(value);
// })
// console.log(promise);
// let res = promise.then(val => { // pending  then 不执行
//     console.log(val);
//     return 3
// })

// setTimeout(() => {
//     console.log(promise)
// })

// const promise = new MyPromise((resolve, reject) => {
//     resolve(100)
// })
// const p1 = promise.then(value => {
//     console.log(value)
//     return p1
// })
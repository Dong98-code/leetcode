// MyPromise.js

const PENDING = 'pending';
const FULLFILLED = 'fullfilled';
const REJECTED = 'rejected';

class MyPromise {
    constructor(executor) {
        // 立即执行 exector
        executor(this.resolve, this.reject);
    }
    //状态值， 初始为PENDING
    status = PENDING;
    // resolve和reject为什么要用箭头函数？
    // 如果直接调用的话，普通函数this指向的是window或者undefined
    // 用箭头函数就可以让this指向当前实例对象
    // 成功之后的值
    value = null;
    reson = null;

    resolve = (value) => {
        // 改变状态和成功后的值
        if (this.status === PENDING) {
            this.status = FULLFILLED;
            this.value = value;
        }
    }

    reject = (reson) => {
        if (this.status === PENDING) {
            this.status = REJECTED;
            this.reson = reson;
        }
    }

    then(onFullfilled, onRejected) {
        // 判断状态
        if (this.status === FULLFILLED) {
            // 调用成功回调，并且把值返回
            onFullfilled(this.value);
        } else if (this.status === REJECTED) {
            // 调用失败回调，并且把原因返回
            onRejected(this.reason);
        }
    }



}
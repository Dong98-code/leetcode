## 浏览器是多线程的：
- GUI渲染线程；渲染和解析页面
- JS引擎线程：渲染和解析JS， 浏览器分配一个线程解析JS，JS为单线程
- 定时器监听线程
- 时间监听线程
- HTTP网络请求线程：同源请求下，浏览器最多分配5-7个http线程

## JS异步任务

1. 异步微任务

- requestAnimationFrame() 争议
- Promise.then/catch/finally
- async / await
- queueMicrotask 手动创建一个异步的微任务
- MutationObserver dom属性值改变
- IntersectionObserver 当前dom元素和可视窗口交互发生的一些变化
- process.nextTick

2.异步宏任务

- 定时器 ： setTimeout/setInterval
- 事件绑定/队列
- XMLHttpRequest/Fetch
- messageChannel 消息队列
- setImmediate 

JS单线程如何实现异步操作？

> 借用浏览器的多线程和EventLoop来实现异步操作；
> 实现单线程异步效果

## 示例
1.

```js
setTimeout(() => {
    console.log(1);
}, 20);
console.log(2); // 同步
setTimeout(() => {
    console.log(3);
}, 10)
console.log(4); // 同步
console.time("aa");
for (let i = 0; i < 100000000; i++) {
    ///
}

console.timeEnd("aa");

console.log(5);//同步

setTimeout(() => {
    console.log(6);
}, 8)

console.log(7); //同步
setTimeout(() => {
    console.log(8);
}, 15)

console.log(9);//同步
console.log("end");//同步
```
输出：
> 2 4 5 7 9 3 1 6 8

解释：
浏览器 加载页面任务，除了开辟堆栈内存之外，还开辟了两个队列： WebAPI和EventQueue
- 执行环境栈：js引擎线程，自上而下解析主线程；
创建两个队列：
- WebAPI:任务监听队列，监听异步任务是否可执行
- EventQueue:事件/任务队列 所有可执行的异步任务 需要在这里任务执行队列排队，在同步任务执行完毕之后，执行可执行的异步任务；

- 执行流程：
  1. 当主线程自上而下执行代码时候，如果遇到监异步任务， 把异步任务放到任务监听队列：
     - 浏览器开启新的线程是否可以执行，不会阻碍主线程的渲染，他会继续向下执行同步代码；
  2. 当异步任务可以执行之后，不会立即执行，而是将其移动到EventQueue中，放到任务队列中
     - 根据宏任务和微任务队列进行区分，放入对应的异步任务队列；
     - 谁先进来排队，谁在各自队伍的最前面
     - 对于定时器，设定一个等待时间，到时间后并不一定会立即去执行，只有同步代码执行完，才会执行异步任务；
  3. 当同步代码执行完，主线程空闲下来之后，此时会去任务队列中，按照顺序执行异步任务：异步微任务优先级较高。相同优先级 谁先放入谁执行；把任务放到栈中执行，只要这个任务没有执行完，不会再去执行其他任务
   


![20220729183839](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729183839.png)

2. 加入Promise的时间队列
   
- promise中的同步异步编程
   ![20220729185742](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729185742.png)

   ![20220729190036](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729190036.png)

- async/await中的同步异步编程


立即执行其后面的代码， 看返回的Promise示例， 如果不是Pormise示例，也会边长promise实例；
会把当前上下文中，await下面的代码代称异步微任务，进入到WebAPI中去监听， 只有后面的实例的状态是成功的，才可以去执行；可执行则进入到EventQueue中去
输出: 
![20220729190657](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729190657.png)
> 1 3 2

3. example2.js

```js
async function async1() {
    console.log("async1 start");
    await async2();
    console.log("async1 end");
}

async function async2() {
    console.log("async2");
}

console.log("script start");
setTimeout(() => {
    console.log("setTimeout");
}, 0)

async1();
new Promise(function (resolve) {
    console.log("promise1");
    resolve();
}).then(function () {
    console.log('promise2');
});
console.log("script end");
// console.log('1111');
```
![20220729200438](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729200438.png)
输出：![20220729200554](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729200554.png)

4. 点击事件回调

```js
let body = document.body;
body.addEventListener('click', function () {
    Promise.resolve().then(() => {
        console.log(1);
    })
    console.log(2);
})

body.addEventListener('click', function () {
    Promise.resolve().then(() => {
        console.log(3);
    })
    console.log(4);
})
```

结果分析：

![20220729202051](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729202051.png)

4. example4.js

```js
function func1() {
    console.log('func1 start');
    return new Promise(resolve => {
        resolve("ok");
    })
}
function func2() {
    console.log('func2 start');
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("ok")
        },10)
    })
}

console.log(1);
setTimeout(async () => {
    console.log(2);
    await func1();
    console.log(3);
}, 20)

for (let i = 0; i < 900000000; i++) { } // 80ms
console.log(4);
func1().then(result => {
    console.log(5);
});
func2().then(result => {
    console.log(6);
})

setTimeout(() => {
    console.log(7); 
}, 0)

console.log(8);

```
输出：
![20220729203447](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729203447.png)

5. example5.js

```js
setTimeout(() => {
    console.log("a");
})

Promise.resolve().then(() => {
    console.log("b");
}).then(
    () => {
        const data = Promise.resolve("c");
        setTimeout(() => {
            console.log("d");
        });
        console.log("f");
        return data;
    }
).then(data => {
    console.log(data);
})
```

输出结果：

![20220729205204](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729205204.png)

6. example.js

```js
console.log("start");
let intervalId;

Promise.resolve().then(() => {
    console.log("p1");

}).then(() => {
    console.log("p2");
})

setTimeout(() => {
    Promise.resolve().then(() => {
        console.log("p3");
    }).then(() => {
        console.log('p4');
    });
    intervalId = setInterval(() => {
        console.log('interval');
    }, 3000)
    console.log("timeout1");
}, 0)
```

输出：
之后没隔3s输出一个"interval"
![20220729211955](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220729211955.png)
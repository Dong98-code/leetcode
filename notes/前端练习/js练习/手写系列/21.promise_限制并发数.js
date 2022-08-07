/*
有8个图片资源的url，已经存储在数组urls中。

urls类似于['https://image1.png', 'https://image2.png', ....]

而且已经有一个函数function loadImg，输入一个url链接，返回一个Promise，该Promise在图片下载完成的时候resolve，下载失败则reject。

但有一个要求，任何时刻同时下载的链接数量不可以超过3个。

请写一段代码实现这个需求，要求尽可能快速地将所有图片下载完成。
*/
var urls = [
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/AboutMe-painting1.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/AboutMe-painting2.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/AboutMe-painting3.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/AboutMe-painting4.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/AboutMe-painting5.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/bpmn6.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/bpmn7.png",
    "https://hexo-blog-1256114407.cos.ap-shenzhen-fsi.myqcloud.com/bpmn8.png",
];

function loadImg(url) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = function () {
            console.log("一张图片加载完成");
            resolve(img);
        };
        img.onerror = function () {
            reject(new Error('Could not load image at' + url));
        };
        img.src = url;
    });
}

function limitLoad(urls, handler, limit) {
    let seq = [].concat(urls); //复制 urls;
    let promises = seq.slice(0, limit).map((url, index) => {
        return handler(url).then(() => {
            // 处理完之后， 返回对应的索引
            return index;
        })
    })

    return seq.reduce((pCollect, url) => {
      return pCollect.then(() => {
          return Promise.race(promises); // 返回已经完成的下标
        }).then(fastestIndex => { // 获取到已经完成的下标
        	// 将"容器"内已经完成的那一项替换
          promises[fastestIndex] = handler(url).then(
            () => {
              return fastestIndex; // 要继续将这个下标返回，以便下一次变量
            }
          );
        }).catch(err => {
          console.error(err);
        });
    }, Promise.resolve()) // 初始化传入
    .then(() => { // 最后三个用.all来调用
      return Promise.all(promises);
    });
}


/*
    poolLimit: 可同时发起请求的最大数量
    array: 将依次作为 iteratorFn 的参数执行
    iteratorFn 一个函数 需要返回 Promise
*/
// es7版本
async function asyncPool(poolLimit, array, iteratorFn) {
    // 最终传给 Promise.all 
    const ret = [] 
    // 正在执行的任务 -就是还没有被解决的 Promise 数组, 这里的 Promise 处于 pending 状态 -限制最大数量就靠它了
    const executing = new Set()
    
    // ES6 迭代 -数组可被 `for of` 迭代, 对象不可以
    for (const [index, item] of array.entries()) { 
        // 每次迭代 都向结果 push 新的 Promise  至于为什么又套了一层 Promise.resolve(), 是为了防止使用的时候没有传入 Promise 导致后续代码执行错误
        console.log(index+1);
        // console.log(`正在执行栈中的任务为${executing.size}`);
        const p = Promise.resolve().then(() => iteratorFn(item, index))
        ret.push(p)

        // 限制并发的逻辑
        if (poolLimit <= array.length) {
            /* 
                在 then 的回调函数中, 当这个 Promise 被解决后, 由 pending 变为 fulfilled 
                已经拿到了服务端数据, 就删除该 Promise，腾出地方添加下一个 Promise，始终保持 executing 内有两个元素
                then 的回调是异步, 别认为 `splice` 在 `executing.push(e)` 的上边很奇怪 
                
                // 感觉这样写也可以呢，为什么要又定义一个变量 e 呢
                p.then(() => executing.splice(executing.indexOf(p), 1))
                executing.push(p)
            */
            const e = p.then(() => executing.delete(e))
            executing.add(e)

            /*
                当正在执行的任务到达限制数量的时候, 利用 await 等待执行
                Promise.race 的作用: 假如 poolLimit 是 2, executing 的任务有任意一个被解决, 
                Promise.race 就是 fulfilled 状态, 之后进入第 3 次 for 循环
            */
            if (executing.size >= poolLimit) {
                await Promise.race(executing)
            }
        }
    }
    // 最后按顺序返回结果
    return Promise.all(ret)
}

// es 9 使用 set 和 迭代器
async function* asyncPool2(concurrency, iterable, iteratorFn) {
    const executing = new Set();
    async function consume() {
      const [promise, value] = await Promise.race(executing);
      executing.delete(promise);
      return value;
    }
    for (const item of iterable) {
      // Wrap iteratorFn() in an async fn to ensure we get a promise.
      // Then expose such promise, so it's possible to later reference and
      // remove it from the executing pool.
      const promise = (async () => await iteratorFn(item, iterable))().then(
        value => [promise, value]
      );
      executing.add(promise);
      if (executing.size >= concurrency) {
        yield await consume();
      }
    }
    while (executing.size) {
      yield await consume();
    }
  }
  

const handler = (url, index) => {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(`任务${url}完成`)
        }, (10-index)*2000)
    }).then(res => {
        console.log('外部逻辑', res);
    })
}
asyncPool(5, urls, handler)
// const timeout = i => new Promise(resolve => setTimeout(() => resolve(i), i));
// asyncPool(2, [1000, 5000, 3000, 2000], timeout);

// for (let i = 0; i < 10; i++) {
//     setTimeout(() => {
//         console.log(i);
//     },(10-i)*100, i)
// }
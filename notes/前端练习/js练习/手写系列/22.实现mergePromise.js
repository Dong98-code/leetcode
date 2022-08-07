// 实现mergePromise函数，把传进去的数组按顺序先后执行，并且把返回的数据先后放到数组data中。

const time = (timer) => {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve()
      }, timer)
    })
  }
  const ajax1 = () => time(2000).then(() => {
    console.log(1);
    return 1
  })
  const ajax2 = () => time(1000).then(() => {
    console.log(2);
    return 2
  })
  const ajax3 = () => time(1000).then(() => {
    console.log(3);
    return 3
  })
  
// async function mergePromise (arr) {
//     // 在这里写代码
    
//     let res = [];
//     for (let ajax of arr) {
//         let value = await ajax();
//         res.push(value);
//     }
//     return Promise.resolve(res)
//   }
  
function mergePromise(arr) {
    let data = [];
    let promise = Promise.resolve();
    for (let ajax of arr) {
        // ajax是一个函数， .then的返回值和 ajax的然会值是一样的
        promise = promise.then(ajax).then(res => {
            data.push(res);
            return data;
        })
    }
    return promise;
}
  mergePromise([ajax1, ajax2, ajax3]).then(data => {
    console.log("done");
    console.log(data); // data 为 [1, 2, 3]
  });
  
  // 要求分别输出
  // 1
  // 2
  // 3
  // done
  // [1, 2, 3]
  
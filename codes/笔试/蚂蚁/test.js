// 题目：实现一个工厂函数，对形参个数固定的函数，能够返回它的柯里化版本。
function curry(func) {
  // TODO

  // 此题要求不查阅资料。
  // 提示：
  // - function(...args) { console.log(args) } 可以取到一个函数的实参
  // - func.length 可以取到 func 的形参个数

  // 返回 函数
  let len = func.length; // 3;
  let curArgs = Array.from(arguments).slice(1); // ?

  return function () {
    let args = curArgs.concat(...arguments);
    if (args.length >= len) {
      // 执行函数
      return func.apply(this, args);
    } else {
      return curry.call(this, func, ...args);
    }
  };
}

// 验证：把 multiply 传递给 curry 函数
function multiply(a, b, c) {
  return a * b * c;
}
let curried = curry(multiply);
console.log(curried(2)(3)(4)); // 24
console.log(curried(2, 3)(4)); // 24
console.log(curried(2, 3, 4)); // 24
console.log(curried(5)(6, 7)); // 210

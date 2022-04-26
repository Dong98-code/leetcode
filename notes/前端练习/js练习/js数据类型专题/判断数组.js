let a = [12]
console.log(Array.isArray(a));
// 原型链
console.log(a.__proto__ === Array.prototype)

// 实例是否属于构造函数

console.log(a instanceof Array);

// constructor

console.log(a.constructor === Array);

// Object.getPrototypeOf

console.log(Object.getPrototypeOf(a) === Array.prototype);

// Array.prototype.isPrototypeOf

/// Object.prototypr.toString().call()
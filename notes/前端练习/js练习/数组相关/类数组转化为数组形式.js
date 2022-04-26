// 1. Array.from()

// args表示一个arguments

Array.from(args)

// 2. 扩展运算符

// [...args]

// concat

Array.prototype.concat.apply([], args)

// slice

Array.prototype.slice.call(args)
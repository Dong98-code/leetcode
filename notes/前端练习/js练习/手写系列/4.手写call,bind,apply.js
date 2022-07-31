var name = '一尾流莺'
var obj = {
    name: 'warbler',
}
var age = 10
var obj = {
  age: 20,
}
function foo() {
    console.dir(this);
    return 'success'
}

function foo_2(a, b) {
    console.dir(this.age + a + b);
}
//// 首先判断输入进来的ctx的类型
// 1. 值类型， 返回对应的构造函数的实例
// 2. 传入的为对象， 返回对象；
// 3. 传入undefined, null或者空对象；

Function.prototype._call = function (ctx, ...args) {

    const o = ctx == undefined ? window : Object(ctx); //使用 Object方法包装ctx


    // 把函数foo赋值给对象o的一个属性  用这个对象o去调用foo  this就指向了这个对象o
    // 下面的this就是调用_call的函数foo  我们把this给对象o的属性fn 就是把函数foo赋值给了o.fn
    //给context新增一个独一无二的属性以免覆盖原有属性
    const key =Symbol() // 独一无二的属性；
    o[key] = this; // 调用者为一个函数， this就是指向这个调用者， o[key]就是这个调用者

    const result = o[key](...args);
    delete o[key]; // 删除这个属性
    return result;


}

// console.log(foo._call(undefined)) // window
// foo._call(null) // window
// foo._call(1) // Number
// foo._call('11') // String
// foo._call(true) // Boolean
// foo._call(obj) // {name: 'warbler'}
// console.log(foo._call(obj)); // success

Function.prototype._apply = function(ctx, args = []) {
    const o = ctx == undefined ? window : Object(ctx);
    const key = Symbol();
    o[key] = this;
    const result = o[key]([...args]);
    delete o[key];
    return result;
}
console.log(foo_2(3, 4)) // => 17
console.log(foo_2._apply(obj, [3, 4])) //=> 27
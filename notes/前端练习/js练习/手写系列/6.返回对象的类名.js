
/*
获取数据的类型
1. instanceOf 判断某一个构造函数的prototype是否出现在实例对象的原型链上
2. constructor

检测构造函数：
null和undefined没有constructor;
判断数字时使用(),比如 (123).constructor,如果写成123.constructor会报错
constructor在类继承时会出错,因为Object被覆盖掉了,检测结果就不对了


3. Object.proptype.toString.call()
    Object.prototype.toString.call(new Date()) // [object Date]
    Object.prototype.toString.call("1") // [object String]
    Object.prototype.toString.call(1) // [object Numer]
    Object.prototype.toString.call(undefined) // [object Undefined]
    Object.prototype.toString.call(null) // [object Null]
*/

function myTypeOf(data) {
    let toString = Object.prototype.toString;
    let dataType =  toString.call(data).replace(/\[object\s(.+)\]/,"$1");
    if (dataType === 'Object') {
        return data.constructor.name;
    }
    return dataType
}

console.log(myTypeOf({ a:1}));


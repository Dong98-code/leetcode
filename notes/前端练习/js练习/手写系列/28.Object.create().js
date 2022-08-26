//
// Object.myCreate = (proto, propertyObj) => {
//     // 对proto进行判断 null除了基本类型包装对象以外 的对象 不能市 此外就会抛出戳五

// }

Object.ObjectCreate = (proto, propertiesObject)=> {
    // 对输入进行检测
    if (typeof proto !== 'object' && typeof proto !== 'function' && proto !== null) {
        throw new Error(`Object prototype may only be an Object or null:${proto}`);
    }
    // 新建一个对象
    const result = {};
    // 将该对象的原型设置为proto
    Object.setPrototypeOf(result, proto);
    // 将属性赋值给该对象
    Object.defineProperties(result, propertiesObject);
    // 返回该对象
    return result;
}
let a = new String('a')
console.log(typeof a)

console.log("a" === a);

let c = Object.create(a)
console.log(c);
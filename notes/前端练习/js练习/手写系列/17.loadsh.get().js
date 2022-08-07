/**
 * Gets the value at `path` of `object`. If the resolved value is
 * `undefined`, the `defaultValue` is returned in its place.
 *
 * @since 3.7.0
 * @category Object
 * @param {Object} object The object to query.
 * @param {Array|string} path The path of the property to get.
 * @param {*} [defaultValue] The value returned for `undefined` resolved values.
 * @returns {*} Returns the resolved value.
 * @see has, hasIn, set, unset
 * @example
 *
 * const object = { 'a': [{ 'b': { 'c': 3 } }] }
 *
 * get(object, 'a[0].b.c')
 * // => 3
 *
 * get(object, ['a', '0', 'b', 'c'])
 * // => 3
 *
 * get(object, 'a.b.c', 'default')
 * // => 'default'
 */

function baseGet(object, path) {
    //path为数组或者Object
    let newPath = [];
    if (Array.isArray(path)) {
        newPath = path;
    } else {
        // 将路径中的.替换为 [ , ] -> ""
        newPath = path.replace(/\[/g, ".").replace(/\]/g, "").split(".");
    }
    // 
    return newPath.reduce((o, k) => { return (o || {})[k]}, object) // 中途出现undefin 使用空对象继续函数
}

function get(object, path, defaultValue) {
    const result = object == null ? undefined : baseGet(object, path); // object为null,返回 undefined
    return result === undefined ? defaultValue : result; //defaultValue没设置 默认为undefined

}

const object = { 'a': [{ 'b': { 'c': 3 } }] }

let res1 = get(object, 'a[0].b.c')
console.log(res1);
 // => 3

//  get(object, ['a', '0', 'b', 'c'])
//  // => 3

//  get(object, 'a.b.c', 'default')
//  // => 'default'
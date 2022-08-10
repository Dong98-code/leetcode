const obj = {
	a: {
  	b: 1,
		c: 2,
		d: {
			e: 5
		}
  },
  b: [1, 3, {a: 2, b: 3}],
  c: 3
}
// {
//   'a.b': 1,
//   'a.c': 2,
//   'a.d.e': 5,
//   'b[0]': 1,
//   'b[1]': 3,
//   'b[2].a': 2,
//   'b[2].b': 3
//    c: 3
// }
function isFunction(obj) {
    return typeof obj === "function";
}

function flatten(obj) {
    let res = {}

    // 遍历
    function baseFlatten(item, preKey="") {
        for (let [key, value] of Object.entries(item)) {
            let newKey = key;
            if (Array.isArray(item)) {
                // 对应的值为数组
                newKey = preKey ? `${preKey}[${key}]` : key;
            } else {
                newKey = preKey ? `${preKey}.${key}` : key
            }

            if (value && typeof value === 'object'){
                baseFlatten(value , newKey)
              }else{
                res[newKey] = value
              }
        
        }
    }

    baseFlatten(obj);
    return res;
    
}

console.log(flatten(obj));
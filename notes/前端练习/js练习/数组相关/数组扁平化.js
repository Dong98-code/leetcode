// 数组[] [1, [2, [3, 4]]];
// 变成 [1, 2, 3, 4, 5]
//#region
// function flatten(arr) {
//     let res = [];
//     for (let ele of arr) {
//         if (Array.isArray(ele)) {
//             res = res.concat(flatten(ele));
//         } else {
//             res.push(ele);
//         }
//     }
//     return res;
// }
//#endregion
// console.log(flatten([1, [2, [3, 4]]]));
// console.log([].concat(...[1]));
// console.log([].concat(...[1, [2, [3, 4]]]));
// 展开运算符 为浅拷贝 原来的数组， 所以没有办法进行多层的展开
// array = [1, [2, [3, 4]]];
// function flatten(arr) {
//     while (arr.some(item => Array.isArray(item))) {
//         arr = [].concat(...arr);

//     }
//     return arr;
// }

var arr1 = [1,2,3,[1,2,3,4, [2,3,4]]];
function flatten(input) {
  const stack = [...input];
  const res = [];
  while (stack.length) {
    // 使用 pop 从 stack 中取出并移除值
    const next = stack.pop();
    if (Array.isArray(next)) {
      // 使用 push 送回内层数组中的元素，不会改动原始输入
      stack.push(...next);
    } else {
      res.push(next);
    }
  }
  // 反转恢复原数组的顺序
  return res.reverse();
}
flatten(arr1);// [1, 2, 3, 1, 2, 3, 4, 2, 3, 4]
// console.log(flatten(array));

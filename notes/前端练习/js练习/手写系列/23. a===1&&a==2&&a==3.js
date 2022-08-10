// a == 1 && a == 2 && a == 3 可能为 true 吗？
// 隐式转换在干什么？
// 当左边为对象， 右为数字， 尝试调用 toString(), 返回值 再比较
const a = {
    value : 0,
    toString: function () {
        // 调用一次， 自身的value + 1
        return a.value += 1;
    }
}

console.log(a == 1 && a == 2 && a == 3);
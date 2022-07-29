//实现 rand() 4: 生成[0, 4]的随机整数
let rand4 = function () {
    let min = Math.ceil(0);
    let max = Math.floor(4);
    return Math.floor(Math.random() * (max - min + 1)) + min; //含最大值，含最小值
}

console.log(rand4());
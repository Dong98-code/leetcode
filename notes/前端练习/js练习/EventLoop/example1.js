setTimeout(() => {
    console.log(1);
}, 20);
console.log(2); // 同步
setTimeout(() => {
    console.log(3);
}, 10)
console.log(4); // 同步
console.time("aa");
for (let i = 0; i < 100000000; i++) {
    ///
}

console.timeEnd("aa");

console.log(5);//同步

setTimeout(() => {
    console.log(6);
}, 8)

console.log(7); //同步
setTimeout(() => {
    console.log(8);
}, 15)

console.log(9);//同步
console.log("end");//同步

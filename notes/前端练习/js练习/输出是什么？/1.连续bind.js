var bar = function(){
    console.log(this.x);
}
var foo = {
    x:3
}
var sed = {
    x:4
}

var func = bar.bind(foo).bind(sed);
// console.log(func.this);
// func(); //?
console.log(func());
// bind只能使用一次
// var fiv = {
//     x:5
// }
// var func = bar.bind(foo).bind(sed).bind(fiv);
// func(); //?
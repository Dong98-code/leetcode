// function curry(fn, curArgs) {
//     // 返回一个新的fun
//     return function () {
//         let args = Array.from(arguments); // arguments转换为数组形式；
//         if (curArgs !== undefined) {
//             args = args.concat(curArgs);

//         }
//         // 递归调用
//         if (args.length < fn.length) {
//             // function。length为函数必须要传入的参数的个数；
//             return curry(fn, args);
//         }

//         return fn.apply(null, args);
//     }
// }

// function sum (a, b, c) {
//     // console.log(a + b + c);
//     return a + b + c;
// }
// // console.log(sum.length);


// const fn = curry(sum)
// // console.log(typeof fn); // function, 匿名函数， fn.length = 0
// // console.log(fn);
// console.log(fn(1)(2));

// 事件监听方法
// 固定一些参数， 参数复用
// const whichEvent = (function () {
//     if (window.addEventListener) {
//         return function (ele, type, listener, userCapture) {
//             ele.addEventListener(type, function (e) {
//                 listener.call(ele, e); // 改变this指向 为ele
//             }, userCapture);
//         }
//     } else {
//         return function (ele, type, handler) {
//             ele.attachEvent('on' + type, function (e) {
//                 handler.call(ele, e);
//             })
//         }
//     }
// })();

//延迟执行

// add参数不确定

const add = function (args) {
    // args传入的为数组形式的参数
    return args.reduce((a, b) => a + b);

}

// console.log(add(1, 2, 3, 4));

const foo = function (...args1) {
    const sum1 = add(args1);
    // return sum1;
    const fn = function (...args2) {
        const sum2 = add(args2);
        return foo(sum1 + sum2);
    }
    fn.toString = () => {
        return sum1;
    }
    return fn;
}

// 函数的参数值是定长的， 则可以通过原来的函数的参数个数来判断是否继续递归

// function curry(fn, curArgs) {
//     // 返回一个函数
//     return function () {
//         let args = Array.from(arguments);
//         if (curArgs !== undefined) {
//             // args = args.concat(curArgs);
//             args = curArgs.concat(args);
//         }

//         //递归
//         if (args.length < fn.length) {
//             return curry(fn, args);
//         }

//         return fn.apply(null, args);
//     }


// }


const curry = function (fn, curArgs) {
    return function () {
        let args = Array.from(arguments);
        if (curArgs !== undefined) {
            args = curArgs.concat(args);

        }
        if (args.length < fn.length) {
            return curry(fn, args);
        }

        return fn.apply(null, args);
    }
}
function sum(a, b, c) {
    // console.log(a + b + c);
    return a + b + c;
}

const f = curry(sum);

// console.log(f(4,3)(2));

const persons = [
    { name: 'kevin', age: 4 },
    { name: 'bob', age: 5 }
];

// 这里的 curry 函数，之前已实现
const getProp = curry(function (obj, index) {
    const args = [].slice.call(arguments);
    return obj[args[args.length - 1]];
});

// const ages = persons.map(getProp('age')); // [4, 5]
// const names = persons.map(getProp('name')); // ['kevin', 'bob']

// console.log(ages);

const getProp2 = curry(function (obj, key) {
    return obj[key];
})

const ages = persons.map(el => {
    return getProp2(el)('age');
})

console.log(ages);




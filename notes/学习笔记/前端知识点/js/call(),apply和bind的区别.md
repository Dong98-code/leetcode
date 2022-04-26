
[链接](https://juejin.cn/post/6971029774995030029)

[this,call,bind, apply](https://juejin.cn/post/6844903496253177863)

## this的指向

> this永远指向最后调用它的对象；

```js
    var name = "windowsName";
    function a() {
        var name = "Cherry";

        console.log(this.name);          // windowsName

        console.log("inner:" + this);    // inner: Window
    }
    a();
    console.log("outer:" + this)         // outer: Window
```

![20220411185259](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411185259.png)

```js
    var name = "windowsName";
    var a = {
        name: "Cherry",
        fn : function () {
            console.log(this.name);      // Cherry
        }
    }
    a.fn();
```

fn()最后由a调用， 函数里面的this为对象`a`

```js
var name = "windowsName";
    var a = {
        name: "Cherry",
        fn : function () {
            console.log(this.name);      // Cherry
        }
    }
    window.a.fn(); // 最后调用它的对象仍然为对象a
```

![20220411185514](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411185514.png)

## 改变this的指向

![20220411185715](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411185715.png)

```js

    var name = "windowsName";

    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)     
        },

        func2: function () {
            setTimeout(  function () {
                this.func1()
            },100);
        }

    };

    a.func2()     // this.func1 is not a function
```

### 箭头函数

箭头函数并不会改变this的指向：
> 箭头函数需要记着这句话：“箭头函数中没有 this 绑定，必须通过查找作用域链来决定其值，如果箭头函数被非箭头函数包含，则 this 绑定的是最近一层非箭头函数的 this，否则，this 为 undefined”。

示例：

```js
    var name = "windowsName";

    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)     
        },

        func2: function () {
            setTimeout( () => {
                this.func1() // 为func2的this
            },100);
        }

    };

    a.func2()     // Cherry
```

![20220411190146](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411190146.png)


### apply call  bind

apply
```js
    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)
        },

        func2: function () {
            setTimeout(  function () {
                this.func1()
            }.apply(a),100);
        }

    };

    a.func2()            // Cherry

// call
    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)
        },

        func2: function () {
            setTimeout(  function () {
                this.func1()
            }.call(a),100);
        }

    };

    a.func2()            // Cherry

// bind

    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)
        },

        func2: function () {
            setTimeout(  function () {
                this.func1()
            }.bind(a),100);
        }

    };

    a.func2()            // Cherry
```

#### apply

[定义](https://juejin.cn/post/6844903496253177863)：

![20220411190433](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411190433.png)

语法：

> func.apply(thisArg, [argsArray])

thisArg：在 fun 函数运行时指定的 this 值。需要注意的是，指定的 this 值并不一定是该函数执行时真正的 this 值，如果这个函数处于非严格模式下，则指定为 null 或 undefined 时会自动指向全局对象（浏览器中就是window对象），同时值为原始值（数字，字符串，布尔值）的 this 会指向该原始值的自动包装对象。

argsArray：一个数组或者类数组对象，其中的数组元素将作为单独的参数传给 fun 函数。如果该参数的值为null 或 undefined，则表示不需要传入任何参数。从ECMAScript 5 开始可以使用类数组对象。浏览器兼容性请参阅本文底部内容

#### call apply

传入的参数不同

> fun.call(thisArg[, arg1[, arg2[, ...]]])

```JS
// apply
    var a ={
        name : "Cherry",
        fn : function (a,b) {
            console.log( a + b)
        }
    }

    var b = a.fn;
    b.apply(a,[1,2])     // 3， 传入类数组或者数组形式的参数；
// call
    var a ={
        name : "Cherry",
        fn : function (a,b) {
            console.log( a + b)
        }
    }

    var b = a.fn;
    b.call(a,1,2)       // 3 , 传入的为参数列表；
```

#### bind的不同之处

```js
    var a ={
        name : "Cherry",
        fn : function (a,b) {
            console.log( a + b)
        }
    }

    var b = a.fn;
    b.bind(a,1,2)()           // 3, 创建新的函数， 手动调用；
```

#### js中的函数调用

函数调用的方法一共有 4 种

作为一个函数调用
函数作为方法调用
使用构造函数调用函数
作为函数方法调用函数（call、apply）

1. 作为函数调用

就是一个简单的函数， 再非严格模式下属于 全局对象 window的， 在严格模式下， undefined；

2. 函数作为方法调用：
   
   作为对象的方法调用；

   ![20220411191413](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411191413.png)

![20220411191528](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411191528.png)

new的过程：

1. 创建一个新的空对象obj
2. 创建的对象的隐式原型 指向其构造函数的显示原型；
3. 使用 call改变 this的指向；
4. 如果无返回值或者返回一个非对象值，则将 obj 返回作为新对象；如果返回值是一个新对象的话那么直接直接返回该对象。

```js
let a = new myFunction("","");

new myFunction{
    let obj={};
    obj.__proto__ = myFunction.prototype;
    let res = myFuntion.call(obj, "li","cherry");
    return typeof result === "obj" ? result : obj;
}
```

#### 作为函数方法调用

![20220411192018](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411192018.png)



```js
var length=10;

function fn() {

console.log(this.length);

}
var obj = {
length:5,

method:function (fn) {

fn();
arguments[0](); // arguments为函数参数的对象， 相当于 arguments.0 ()调用这个函数， 最后的调用者为argument 对象， 所以返回的时argument对象的length;此时只有一个参数， fn 索引返回1；

}

};
obj.method(fn);// 10 1
obj.method(fn,123); // 10 2
```

`arguments`是一个 传递给函数的参数的类数组对象；

```JS
function func1(a, b, c) {
  console.log(arguments[0]);
  // expected output: 1

  console.log(arguments[1]);
  // expected output: 2

  console.log(arguments[2]);
  // expected output: 3
}

func1(1, 2, 3);

```

- ![20220411193635](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411193635.png)


### 手写

#### call 和 apply介绍
参考：
[手写bind, call, apply](https://juejin.cn/post/7030759884542967821)
> 任何函数都可以调用这两个方法，说明它们是添加在函数原型上的方法（Function.prototype）
> 调用 call和apply的函数会立刻执行
> 返回值为函数的返回值；

```js
var name = '一尾流莺'
var obj = {
  name: 'warbler',
}
function foo() {
  console.log(this.name);
  return 'success'
}
foo.call(obj) //=> warbler, this变成obj, log(obj.name)
console.log(foo.call(obj)); // => success

```

> 调用 call 和 apply 指向 undefined 或者 null ，会将 this 指向 window。

![20220411194403](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411194403.png)

> 调用 call 和 apply 指向一个值类型， 会将 this 指向由它们的构造函数创建的实例

![20220411194449](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411194449.png)

> 除了传参的形式不同没什么区别。
传给fn的参数写法不同：
    call 接收多个参数，第一个为函数上下文也就是 this ，后边参数为函数本身的参数。
    apply 接收两个参数，第一个参数为函数上下文 this，第二个参数为函数参数只不过是通过一个 数组 的形式传入的。
    只要记住 apply 是以 a 开头，它传给 fun 的参数是 Array，也是以 a 开头的，就可以很好的分别这两个函数了。


#### bind

![20220411205800](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220411205800.png)

```js
var name = '一尾流莺'
var obj = {
  name: 'warbler',
}

// this 指向调用者document
document.onclick = function() {
  console.dir(this); // => #document
}

// this 指向 obj
document.onclick = function() {
  console.dir(this); // => #Object{name:'warbler}
}.bind(obj)


```

bind返回一个函数 但是并不会立刻执行；

返回 调用它的函数func的拷贝， 并且改变了this的指向， 但是并不会立刻执行它， 需要手动调用；

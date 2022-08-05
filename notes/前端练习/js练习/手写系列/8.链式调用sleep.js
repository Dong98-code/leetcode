/*
实现一个类， 其实例 可以链式调用 sleep方法 sleep一段时间后后续调用

*/
class PlayBoy {
    constructor(name) {
        this.name = name;
        this.queue = [];
        setTimeout(() => {
            // console.log(this.queue.length);
            this.next();
        }, 0)
    }
    next() {
        // 执行队列中存档的函数
        // console.log(1);
        console.log(this.queue.length);
        const fn = this.queue.shift();
        fn && fn(); // fn存在 并执行
    }

    sayHi() {
        const fn = () => {
            // console.log('sayHi');
            // console.log(this.queue);
            console.log(`大家好我是${this.name}`);
            // console.log(this.queue.length);
            this.next();
        }
        // console.log(222);
        this.queue.push(fn);
        // console.log(this);
        return this; // 返回的是当前实例
    }

    sleep(time) {
        const fn = () => {
            setTimeout(() => {
                // console.log(this);
                console.log(`${time}ms后`);
                this.next();
            }, time,time)
        }
        this.queue.push(fn)
        return this;
    }
    play(item) {
        const fn = () => {
            console.log(item);
            this.next()
        }
        this.queue.push(fn);
        return this;
    }
}   

const boy = new PlayBoy("xd")
// console.log(111);
// console.log(boy);
// setTimeout(() => {
//     console.log(boy.sayHi().sleep(1000).play('王者'));
// },1000)
// boy.sayHi().sleep(1000).play('王者').sleep(2000).play('ssss');
boy.sayHi().play('xxx').sleep(2000).sayHi().sayHi().sayHi()



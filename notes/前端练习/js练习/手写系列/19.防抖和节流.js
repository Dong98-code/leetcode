// 防抖 throttle 防抖：debounce
// 节流：顾名思义，在一段时间内只执行一次，若在这期间重复触发，则只有一次生效
//在n秒之后 执行改事件， 若在ns之内 重复触发 则重新计时

function throttle1(fn, delay = 500) {
    // 事件戳
    let preTime = Date.now();
    return function (...args) {
        let curTime = Date.now();
        if (curTime - preTime >= delay) {
            fn.apply(null, args);
            let preTime = Date.now()
        }
    }
}

function throttled2(fn, delay = 500) {
    let timer = null;
    return function (...args) {
        if (!timer) {
            timer = setTimeout(() => {
                fn.apply(this, ...args)
                timer = null;
            }, delay)
        }
    }
}

function debouce1(fn, wait) {
    let timer;
    return function () {
        let _this = this;
        let args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function () {
            fn.apply(_this, args)
        }, wait);
    }
}

function debouce2(fn, wait, immediate) {
    let timer;
    return function () {
        if (immediate) {
            immediate = !immediate;
            fn.apply(this, arguments)
        }
        if (timer) clearTimeout(timer);
        timer = setTimeout(() => {
            fn.apply(this, arguments)
        }, wait);
    }
}

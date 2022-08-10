// 红灯3s亮一次，黄灯两s亮一次， 绿灯1s亮一次
function red() {
    console.log('red');
}
function green() {
    console.log('green');
}
function yellow() {
    console.log('yellow');
}

function wait(time) {
    return new Promise(resolve => setTimeout(resolve, time))
}
async function start() {
    while (1) {
        red();
        await wait(3000);
        green();
        await wait(2000);
        yellow();
        await wait(1000)
    }
}

start()

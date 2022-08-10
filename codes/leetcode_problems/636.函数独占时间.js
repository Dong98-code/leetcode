var exclusiveTime = function(n, logs) {
    // 栈
    let res = new Array(n).fill(0);
    let stack = [];
    for (let log of logs) {
        let [id, flag, time] = log.split(":");
        id = parseInt(id);
        time = parseInt(time);
        if (flag === "start") {
            // 入栈
            stack.push([id, time]); // [id, 开始时间]
        } else {
            // 结束时间
            let [pop_id, start_time] = stack.pop();
            // 如果此时栈为空
            let time_delta = time - start_time + 1;
            res[pop_id] += time_delta;
            if (stack.length !== 0) {
                // 此时栈不为空， 栈顶元素的时间的 - interval
                let peek_id = stack[stack.length-1][0];
                res[peek_id] -= time_delta;
            }
        }
    }
    return res;
};
const n = 2
const logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
console.log(exclusiveTime(n, logs));
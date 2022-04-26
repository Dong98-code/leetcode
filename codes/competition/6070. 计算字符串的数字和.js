var digitSum = function(s, k) {
    while(s.length > k) {
        let arr = s.split("").map(el => +el); // 数组整数
        let tmp = [];
        let cnt = Math.floor(s.length / k)
        for (let i=0;i<cnt;i++) {
            tmp.push(arr.slice(i*k, (i+1)*k).reduce((a,b)=>a+b));
        }
        let tmp_arr = arr.slice(cnt * k, s.length);
        if (tmp_arr.length === 0) {
                    s = tmp.join("");

        } else {
            tmp.push(tmp_arr.reduce((a,b)=>a+b));
                    s = tmp.join("");

        }
    }
    return s;
};

digitSum("11111222223", 2)
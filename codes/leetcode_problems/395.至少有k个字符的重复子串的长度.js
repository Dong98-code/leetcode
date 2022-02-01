/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 var longestSubstring = function(s, k) {
    if (s.length < k) {
        return 0;
    }
    let cnt = new Array(26).fill(0);
    for (let i = 0;i<s.length;i++) {
        cnt[s[i].charCodeAt() - 'a'.charCodeAt()] += 1;
    }
    for (let i=0; i < 26 ; i++) {
        if (cnt[i] > 0 && cnt[i] < k) {
            // i为索引值
            let split = String.fromCharCode(i + 'a'.charCodeAt());
            let res = 0;
            for (let str of s.split(split)) {
                res = Math.max(res, longestSubstring(str, k));
            }
            return res;
        }
    }
    // 原字符串中没有小于k的字符串，返回字符串的长度
    return s.length;
};

console.log(longestSubstring("aaabb", 3));
/**
 * @param {string} word
 * @return {number}
 */
 var countVowelSubstrings = function(word) {
    let ans = 0;
    let n = word.length;
    let dic = ['a','e','i','o','u'];
    if (n <=5 ) {
        return 0;
    }
    for (let i=0;i<n;i++){
        for (let j=i+4;j<n;j++) {
            let sub_str = word.slice(i,j+1);
            let str_set = new Set();
            let good = true;
            for (let s of sub_str) {
                str_set.add(s);
            }
            if (str_set.size == 5) {
                for (let s of str_set) {
                    if (!dic.includes(s)) {
                        good = false;
                        break;
                    }
                }
                if (good) {
                    ans += 1;
                }
            } 
        }
    }
    return ans;
};

console.log(countVowelSubstrings('aeioua'));
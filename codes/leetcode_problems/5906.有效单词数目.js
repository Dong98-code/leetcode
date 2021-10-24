/**
 * @param {string} sentence
 * @return {number}
 */
 var countValidWords = function(sentence) {
    const arr = sentence.split(' ').filter(item => item !== '').map(item => item.trim());
    let cnt = 0;
    let patt = /^[a-z]+-?[a-z]+[!,.]?|[a-z]*[!,.]?$/;
    for (let word of arr) {
        if (patt.test(word)) {
            cnt += 1;
        }
    }
    return cnt;
};
let s = "!this  1-s b8d!";
console.log(countValidWords(s));
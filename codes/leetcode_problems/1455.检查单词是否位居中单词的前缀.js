var isPrefixOfWord = function(sentence, searchWord) {
    sentence = sentence.split(" ");
    let res = -1;
    function isPre(word, searchWord) {
        let l1 = word.length;
        let l2 = searchWord.length;
        if (l1 < l2) return false;
        for (let i = 0; i < l2;i++) {
            if (word[i] !== searchWord[i]) {
                return false;
            }
        }
        return true;

    }
    for (let [i, word] of sentence.entries()) {
        if (isPre(word, searchWord)) {
            res = i+1;
            return res;
        }
        // res = i;
    }
    return -1;
};
console.log(isPrefixOfWord("this problem is an easy problem", "pro"))
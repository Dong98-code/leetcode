var maxNumberOfBalloons = function(text) {
    let cnt = new Map();
    for (let i = 0; i< text.length; i++) {
        cnt.set(text[i],(cnt.get(text[i]) || 0) + 1);
    }
    
    return Math.min(cnt.get('b'), cnt.get('a'), Math.floor(cnt.get('l') / 2), Math.floor(cnt.get('o') / 2), cnt.get('n'));
};

console.log(maxNumberOfBalloons('leetcode'));
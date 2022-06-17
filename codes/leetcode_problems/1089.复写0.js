var duplicateZeros = function(arr) {
    //栈
    let l = 0, r = 0, n = arr.length;
    while (r < n) {
        if (arr[l] == 0) {
            r += 1
        }
        l += 1;
        r += 1;
    }
    // 
    l -= 1
    r -= 1
    while (l !== r) {
        if (arr[l] === 0) {
            if (r < n) arr[r] = 0
            r -= 1;
        }
        arr[r--] = arr[l--]
    }

};

console.log(duplicateZeros([1,0,2,3,0,4,5,0]));
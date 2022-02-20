/**
 * @param {number[]} arr
 * @return {number[]}
 */
 var pancakeSort = function(arr) {
    const reverse = (arr, end) => {
        for (let i = 0, j = end; i < j; i++, j--) {
            let temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp
        }
    }
    // let n = arr.length;
    let res = [];

    for (let n=arr.length;n > 1; n--) {
        // 首先找到最大的值所在的index
        let idx = arr.indexOf(n);
        if (idx == n -1) {
            continue;
        }
        // 反转
        reverse(arr, idx);
        reverse(arr,n-1);
        res.push(idx+1);
        res.push(n);

    }
    return res;
};

console.log(pancakeSort(
    [3,2,4,1]));
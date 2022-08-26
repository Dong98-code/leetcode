// 将一个新的数 和前面的数相比较 只要当前数字小于前一个则和前一个交换位置，然后终止
function insertSort(arr) {
    if(arr == null  || arr.length <= 0){
        return [];
    }
    var len = arr.length;
    for(var i = 1; i < len; i++) {
        for(var j = i - 1; j >= 0 && arr[j] > arr[j + 1]; j--) {
            swap(arr, j, j + 1);
        }
    }
    return arr;
}

function swap(arr, i, j){
    var temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
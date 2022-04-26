/**
 * @param {string} input
 * @return {number}
 */
 var lengthLongestPath = function (input) {
    let res = 0, pre = []
    const arr = input.split('\n').map(a => a.split('\t'))
    arr.forEach(a => {
        let path = []
        a.forEach((b, i) => {
            path.push(b || pre[i])
            if (b.indexOf('.') >= 0) {
                res = Math.max(res, path.join('/').length)
            }
        })
        pre = path
    })
    return res
};
console.log(lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"));
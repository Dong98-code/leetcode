/**
 * @param {number[][]} img
 * @return {number[][]}
 */
 var imageSmoother = function(img) {
    // 池化 pooling, average pool
    // padding 
     let m = img.length;
     let n = img[0].length;
    
    for (let i=0;i< m; i++) {
        let row = img[i];
        img[i] = [0.5, ...row, 0.5];
    }
    let mask = [[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,-1],[0,1],[0,0]]
    img.push(new Array(n+2).fill(0.5));
    img.unshift(new Array(n+2).fill(0.5));
    let res = new Array(m).fill(0).map(ele => []);
    for (let i=1; i<img.length - 1;i++) {
        for (let j =1; j < img[0].length-1;j++) {
            let sum = 0, k = 0;
            for (let [dx, dy] of mask) {
                if (img[i+dx][j+dy] !== 0.5) {
                    sum += img[i+dx][j+dy];
                } else {
                    k += 1;
                }
            }
            // let sum = img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j] +img[i][j+1]+img[i+1][j-1]+img[i+1][j] + img[i+1][j+1];
            res[i-1][j-1] = Math.floor(sum/(9-k));
        }

    }
    return res;
};
console.log(imageSmoother([[100,200,100],[200,50,200],[100,200,100], [100,200,100]]));
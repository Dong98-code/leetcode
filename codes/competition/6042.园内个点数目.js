var countLatticePoints = function(circles) {
    const isValid = function(x, y,i,j, r) {
        let dis = (x-i)*(x-i) + (y-j)*(y-j)
        if (dis <= r*r) {
            return true;
        } else {
            return false;
        }
    }
    let res = new Set();
    for (let [xi, yi, ri] of circles) {
        for (let i = xi - ri; i <= xi + ri; i++) {
            for(let j = yi-ri;j <= yi + ri; j++) {
                if (isValid(i, j, xi, yi, ri)) {
                    res.add("i"+"-"+"j");
                }
            }
        }
    }
    return [...res].length;
};

console.log(countLatticePoints(circles = [[2,2,1]]));
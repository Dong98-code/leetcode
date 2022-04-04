/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var maximumCandies = function (candies, k) {
    const getTotals = function (num) {
        let t = 0;
        for (let c of candies) {
            t += Math.floor(c / num); // 这一对糖果最多可以满足的小孩个数
        }
        return t;
        
    }
    let sum = 0;
    let min = 100000001
    for (c of candies) {
        sum += c;
        min = Math.min(min, c);
    }
    if (sum < k) {
        return 0;
    } else if (sum === k) {
        return 1;
    } else {
        // sum > k , 至少分到一颗
        // 下限为1， 上限为min
        let l = 1, r = min;
        while (l <= r) {
            let mid = l + ((r - l) >> 1);
            // 判断是都mid可以满k个小改
            let total = getTotals(mid);
            if (total > k) {
                l = mid + 1;
            } else if (total <= k) {
                r = mid - 1;
            } 
        }
        return l;
    
    };
};

console.log(maximumCandies(candies = [5, 8, 6], k=3));
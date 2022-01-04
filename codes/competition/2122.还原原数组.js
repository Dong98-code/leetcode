/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var recoverArray = function(nums) {
    nums.sort((a,b)=>a-b) ; // 升序排列
    // return nums;
    let n = nums.length;  //数组的长度
    for (let i=1;i<n;i++) {
        if (nums[i] === nums[0] || (nums[i]-nums[0]) % 2 !== 0) {
            continue;
        }
        // 找到一个可能的k值
        let visited = new Array(n).fill(false);
        let k = Math.floor((nums[i] - nums[0])/2);
        let ans = new Array();
        ans.push(nums[0]+k);
        visited[i] = true;
        visited[0] = true;

        let l = 0, r = i;
        for (let j=1;j<Math.floor(n/2);j++) {
            while (visited[l]) {
                l += 1;
            }
            while (r < n && (visited[r] || nums[r] !== nums[l]+2*k)) {
                r += 1;
            }
            if (r === n) {
                break;
            }
            ans.push(nums[l]+k);
            visited[l] = true;
            visited[r] = true;

        }
        if (ans.length === Math.floor(n/2)) {
            return ans;
        }

    }
    return null;
};

console.log(recoverArray([2,10,6,4,8,12]))
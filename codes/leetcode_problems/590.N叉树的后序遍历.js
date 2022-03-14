var digArtifacts = function(n, artifacts, dig) {
    function isSuperset(set, subset) {
        for (let elem of subset) {
            if (!set.has(elem)) {
                return false;
            }
        }
     return true;
    }

    let dig_set = new Set(dig);
    let res = 0;
    for (let art of artifacts) {
        let [r1, c1, r2, c2] = art;
        // 物件的点
        let art_set = new Set();
        for (let i = r1; i <= r2; i++) {
            for (let j = c1; j <= c2; j++) {
                art_set.add([i, j])
            }
        }
        for (let iem of art_set) {
            if (isSuperset(dig_set, art_set)) {
                res += 1;
            }
        }
    }
    return res;
};
console.log(digArtifacts(2,
    [[0,0,0,0],[0,1,1,1]],
    [[0,0],[0,1]],
    2));
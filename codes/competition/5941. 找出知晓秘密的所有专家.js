/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
 var findAllPeople = function(n, meetings, firstPerson) {
    meetings.sort((a, b)=> a[2] - b[2]); 
    // 按照时间升序排列
    let i = 0;
    // 初始化 结果 集合
    let ans = new Set();
    ans.add(0);
    ans.add(firstPerson);

    while (i < meetings.length) {
        let j = i+1;
        while (j < meetings.length && meetings[j][2]===meetings[i][2]) {
            j += 1;
        }
        // 正序
        for (let idx=i;idx<j;idx++) {
            let p1 = meetings[idx][0];
            let p2 = meetings[idx][1];
            if (ans.has(p1) || ans.has(p2)) {
                ans.add(p1);
                ans.add(p2);
            }
        }
        // 反序
        for (let idx=j-1;idx>=i;idx--) {
            let p1 = meetings[idx][0];
            let p2 = meetings[idx][1];
            if (ans.has(p1) || ans.has(p2)) {
                ans.add(p1);
                ans.add(p2);
            }
        }
        i = j; // 更新i
    }
    return [...ans];
    //  return meetings;
};

n = 4
meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
firstPerson = 3
console.log(findAllPeople(n, meetings, firstPerson));
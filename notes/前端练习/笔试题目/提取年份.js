let str = "And millionaires will hold 46% of total wealth by 2019, the report says. This ratio is likely to increase in 2020.".split(" ");
let res = [];
for (let item of str) {
  let cnt = 0;
  for (let i=0;i<item.length;i++) {
    if (item.charCodeAt(i) >= "0".charCodeAt() && item.charCodeAt(i) <= "9".charCodeAt()) {
      // 不能0开头
      if (cnt === 0 && item.charCodeAt(i) === "0".charCodeAt()) {
        continue;
      } else {
        cnt += 1;
      }
    } else {
      if (cnt === 4) {
        let year = +item.substring(i-cnt, i);
        if (year >= 1000 && year <= 3999) {
          res.push(year);
        }
      }
      cnt = 0;
    }
  }
  if (cnt === 4) {
    let year = +item.substring(item.length-cnt, item.length);
        if (year >= 1000 && year <= 3999) {
          res.push(year);
        }
  }
}
console.log(res.join(" "));;
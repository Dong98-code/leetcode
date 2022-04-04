var __readline = require('readline-sync')
__readline.setDefaultOptions({prompt: ''})
var read_line = __readline.prompt

let n = +(read_line());
let line;
// 根据行列取查询相对应的点
let grid = new Array();
while(line=read_line()) {
  let [x_i, y_i] = read_line().split(" ").map(el => +el);
  grid.push([x_i, y_i])
}
let res = 0;

for (let i = 0; i< n; i++) {
  let up=false, down=false, left=false, right= false;
  let [x, y] = grid[i];
  for (let j = 0;j<n;j++) {
    if (j === i) {
      continue;
    }
    let [x_j, y_j] = grid[j];
    if (x_j === x) {
      if (y_j > y) {
        up = true
      } else {
        down = true;
      }
      
    } else if (y_j == y) {
      if (x_j > x) {
        right = true;
      } else {
        left = true;
      }
    } else {
      continue;
    }
  }
  if (left && right && up && down) {
    res += 1;
  }
}
print(res);
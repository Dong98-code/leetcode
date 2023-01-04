// zhang san san,zhang an sa,zhang hang,zhang seng,zhang sen a
// zhas
function f(str, word) {
  let str_arr = str.split(",");
  let res = [];
  for (let person of str_arr) {
    person = person.split(" ");
    if (dfs(person, 0, word, 0)) {
      res.push(person);
    }
  }
  return res;
}
function dfs(person, pi, exp, ej) {
  // 匹配串
  // arr
  if (pi === person.length || ej === exp.length) {
    return pi === person.length && ej === exp.length;
  }
  let name = person[pi];
  // 首字母不匹配
  if (name[0] !== exp[ej]) {
    return false;
  }
  let cnt = 1;
  while (
    cnt < name.length &&
    ej + cnt < exp.length &&
    name[cnt] === exp[ej + cnt]
  ) {
    if (dfs(person, pi + 1, exp, ej + cnt + 1)) {
      return true;
    }
    cnt += 1;
  }
  return dfs(person, pi + 1, exp, ej + 1);
}

let str1 = "zhang san san,zhang an sa,zhang hang,zhang seng,zhang sen a";
let word = "zhas";

console.log(f(str1, word));

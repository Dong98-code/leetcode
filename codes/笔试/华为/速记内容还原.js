// 速记内容还原：
// 有一种速记方式，针对重复内容有一套独特的缩写规则：
// 重复的部分会被以 "(重复内容)<重复次数>" 形式记录，并且可能存在嵌套缩写关系。不重复的部分按照原样记录。
// 现给一个符合此速记方式的字符串 records，请以字符串形式返回复原后的内容。
// 注： records 仅由小写字母、数字及<, >, (, )组成。

// 输入：records = "abc(d)<2>e"
// 输出："abcdde"
// 解释：字符串中出现 "(d)<2>"，表示 "d" 重复出现 2 次，因此返回复原后的内容 "abcdde"。

// 输入：records = "a(b(c)<3>d)<2>e"
// 输出："abcccdbcccde"
// 解释：字符串中出现 "a(b(c)<3>d)<2>"，其中 "(c)<3>" 表示 "c" 出现 3 次，复原为 "ccc"；"(bcccd)<2>" 表示 "bcccd" 重复出现 2 次，复原为 "bcccdbcccd"。最终返回复原后内容 "abcccdbcccde"

// string UnzipString(string records) {

// }

function f(str) {
  let res = "";
  let i = 0;
  while (i < str.length) {
    if (str[i] === "(") {
      //   let tmp = "";
      let j = i + 1;
      // 找到下一个对应 的右括号
      let cnt_l = 0;
      while (j < str.length) {
        if (str[j] === "(") {
          cnt_l += 1;
          j += 1;
        } else if (str[j] === ")") {
          if (cnt_l === 0) break;
          else {
            j += 1;
            cnt_l -= 1;
          }
        } else {
          j += 1;
        }
      }
      let tmp = str.slice(i + 1, j);
      //   统计个数；
      j += 1;
      let tmp_num = "";
      let k = j + 1;
      while (k < str.length && str[k] !== ">") {
        tmp_num += str[k];
        k += 1;
      }
      // k -> >
      let p_res = f(tmp);
      tmp_num = parseInt(tmp_num);
      for (let x = 0; x < tmp_num; x++) {
        res += p_res;
      }
      i = k + 1;
    } else {
      res += str[i];
      i += 1;
    }
  }
  return res;
}
let records = "abc(d)<2>e";
console.log(f(records));

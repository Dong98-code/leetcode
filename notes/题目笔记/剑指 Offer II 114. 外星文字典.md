## 剑指 Offer II 114. 外星文字典

### 题目描述

<div class="content__1Y2H"><div class="notranslate"><p>现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。</p>

<p>给定一个字符串列表 <code>words</code> ，作为这门语言的词典，<code>words</code> 中的字符串已经 <strong>按这门新语言的字母顺序进行了排序</strong> 。</p>

<p>请你根据该词典还原出此语言中已知的字母顺序，并 <strong>按字母递增顺序</strong> 排列。若不存在合法字母顺序，返回 <code>""</code> 。若存在多种可能的合法字母顺序，返回其中 <strong>任意一种</strong> 顺序即可。</p>

<p>字符串 <code>s</code> <strong>字典顺序小于</strong> 字符串 <code>t</code> 有两种情况：</p>

<ul>
	<li>在第一个不同字母处，如果 <code>s</code> 中的字母在这门外星语言的字母顺序中位于 <code>t</code> 中字母之前，那么&nbsp;<code>s</code> 的字典顺序小于 <code>t</code> 。</li>
	<li>如果前面 <code>min(s.length, t.length)</code> 字母都相同，那么 <code>s.length &lt; t.length</code> 时，<code>s</code> 的字典顺序也小于 <code>t</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["wrt","wrf","er","ett","rftt"]
<strong>输出：</strong>"wertf"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["z","x"]
<strong>输出：</strong>"zx"
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = ["z","x","z"]
<strong>输出：</strong>""
<strong>解释：</strong>不存在合法字母顺序，因此返回 <code>"" 。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 269&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/alien-dictionary/">https://leetcode-cn.com/problems/alien-dictionary/</a></p>
</div></div>


### 解题思路

拓朴排序

![20220531113909](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220531113909.png)


1. 建立邻接表和入度矩阵
2. 使用队列， 从入度为0的节点开始 遍历邻接表， 在这个过程中， 把入度为0的节点 加入到队列中

3. 当队列为空的时候 判断 点的个数 和排序之后的个数是否一致 否则 就说明 存在环

### 代码


```js
/**
 * @param {string[]} words
 * @return {string}
 */
var alienOrder = function(words) {
    // 拓扑排序
    // 建立邻接表和入度矩阵
    let edges = new Map();
    let inDegrees = new Map();
    let l = words.length;
    let isValid = true;
    for (let word of words) {
        let cur_l = word.length;
        for (let i = 0;i< cur_l;i++) {
            if (!edges.has(word[i])) {
                edges.set(word[i], [])  // 确定节点
            }
        }
    }

    // 按照顺序建立邻接表
    const addEdge = function(word1, word2) {
        let l1 = word1.length;
        let l2 = word2.length;
        let min_l = Math.min(l1, l2);
        let idx = 0;
        while (idx < min_l) {
            let c1 = word1[idx], c2 = word2[idx];
            if (c1 !== c2) {
                // 例如 t -> f
                edges.get(c1).push(c2);
                // 入度矩阵
                inDegrees.set(c2, (inDegrees.get(c2) || 0) + 1);
                break; // 之后不能在判定先后顺序
            }
            idx += 1;
        }
        if(idx === min_l && l1 > l2) {
            // abc , ab 这种情况
            isValid = false;
        }
    }

    for (let i = 1; i< l && isValid; i++) {
        addEdge(words[i-1], words[i]);
    }
    if (!isValid) {
        return "";
    }
    let q = [];
    for (let key of edges.keys()) {
        if (!inDegrees.has(key)) {
            q.push(key);// 最开始入度为0的点，作为起点
        }
    }

    let res = [];

    while (q.length) {
        let c = q.shift();
        // 
        res.push(c); // 加入 拓扑序列中
        let adjs = edges.get(c); // 获取相对应的邻接表
        for (let u of adjs) {
            // 对应的入度-1
            inDegrees.set(u, inDegrees.get(u) - 1);
            // 如果此时入度为0
            if (inDegrees.get(u) === 0) {
                q.push(u)
            }
        }

    }
    // 判断是否有环
    return res.length === edges.size ? res.join("") : "";
    
};
```
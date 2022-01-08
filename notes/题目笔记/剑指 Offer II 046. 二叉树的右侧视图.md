## 剑指 Offer II 046. 二叉树的右侧视图
### 题目

链接：
[剑指 Offer II 046. 二叉树的右侧视图](https://leetcode-cn.com/problems/WNC0Lk/)

<div class="content__1Y2H"><div class="notranslate"><p>给定一个二叉树的 <strong>根节点</strong> <code>root</code>，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img style="width: 270px;" src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg"></p>

<pre><strong>输入:</strong>&nbsp;[1,2,3,null,5,null,4]
<strong>输出:</strong>&nbsp;[1,3,4]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>&nbsp;[1,null,3]
<strong>输出:</strong>&nbsp;[1,3]
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong>&nbsp;[]
<strong>输出:</strong>&nbsp;[]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li>二叉树的节点个数的范围是 <code>[0,100]</code></li>
	<li><code>-100&nbsp;&lt;= Node.val &lt;= 100</code>&nbsp;</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 199&nbsp;题相同：<a href="https://leetcode-cn.com/problems/binary-tree-right-side-view/">https://leetcode-cn.com/problems/binary-tree-right-side-view/</a></p>
</div></div>


### 思路

BFS : 遍历每一层， 将每一层最后一个加入到结果 数组中

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root):
        # bfs ，每一层的最后一个
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            length_layer = len(q)
            for i in range(length_layer):
                node = q.popleft()
                if i == length_layer-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
```
js:

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    let q = [];
    let res = [];  // 存储结果
    if (root == null) {
        return [];
    }
    q.push(root)
    while (q.length !== 0) {
        l = q.length;
        for (let i=0;i<l;i++) {
            let node = q.shift();
            if (i == l - 1) {
                res.push(node.val);

            }
            if (node.left !== null) {
                q.push(node.left);
            }
            if (node.right !== null) {
                q.push(node.right);
            }
        }
    }
    return res;
};
```

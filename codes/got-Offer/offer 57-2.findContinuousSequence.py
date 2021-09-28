"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
一共有三种情况：

如果 \textit{sum}<\textit{target}sum<target 则说明指针 rr 还可以向右拓展使得 sumsum 增大，此时指针 rr 向右移动，即 r+=1
如果 sum>targetsum>target 则说明以 ll 为起点不存在一个 rr 使得 sum=targetsum=target ，此时要枚举下一个起点，指针 ll 向右移动，即l+=1
如果 \textit{sum}==\textit{target}sum==target 则说明我们找到了以 ll 为起点得合法解 [l,r][l,r] ，我们需要将 [l,r][l,r] 的序列放进答案数组，且我们知道以 ll 为起点的合法解最多只有一个，所以需要枚举下一个起点，指针 ll 向右移动，即 l+=1
终止条件即为 l>=rl>=r 的时候，这种情况的发生指针 rr 移动到了\lfloor\frac{\textit{target}}{2}\rfloor+1⌊ 
2
target
​	
 ⌋+1 的位置，导致 l<rl<r 的时候区间和始终大于 targettarget 。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/mian-shi-ti-57-ii-he-wei-sde-lian-xu-zheng-shu-x-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res, ans = 1, 2, 3, []
        while i < j:
            if res == target:
                ans.append([x for x in range(i, j + 1)])
                i += 1
                res = res -i+1

            elif res > target:
                i += 1
                res = res - i + 1
            else:
                j += 1
                res += j
        return ans
sol = Solution()
print(sol.findContinuousSequence(9))

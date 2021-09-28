"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def titleToNumber(self, columnTitle):
        lst = list(columnTitle)
        sum = 0
        i = 0
        while lst:
            item = lst.pop(-1)
            sum = sum+(ord(item)-64)*(26**i)
            i += 1
        return sum

s =Solution()
s.titleToNumber('ZY')

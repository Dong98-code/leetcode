"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def relativeSortArray(self, arr1, arr2):
        upper = max(arr1)
        ans = list()
        dic = [0] * (upper + 1)
        for item in arr1:
            dic[item] += 1
        for item in arr2:
            while dic[item] > 0:
                ans.append(item)
                dic[item] -= 1
        for i in range(len(dic)):
            while dic[i] > 0:
                ans.append(i)
                dic[i] -= 1
        return ans
if __name__ == "__main__":
    solu = Solution()
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(solu.relativeSortArray(arr1, arr2))



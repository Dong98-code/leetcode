"""

"""
class Solution:
    def combinationSum(self, candidates, target: int):
        # res = []
        # path = []
        # def backtrack(candidates, target,sum,startIndex):
        #     if sum > target:
        #         return
        #     if sum == target:
        #         # if path not in res:
        #             return res.append(path[:])
        #     for i in range(startIndex, len(candidates)):
        #         if i > startIndex and candidates[i] == candidates[i - 1]:
        #             continue
        #         if sum + candidates[i] > target:
        #             return  # 如果 sum + candidates[i] > target 就终止遍历
        #         sum += candidates[i]
        #         path.append(candidates[i])
        #         backtrack(candidates, target, sum, i+1)  # startIndex = i:表示可以重复读取当前的数
        #         sum -= candidates[i]  #回溯
        #         path.pop()  # 回溯
        # candidates = sorted(candidates)  # 需 要排序
        # backtrack(candidates, target, 0, 0)
        # return res
        path = []
        res = []
        candidates.sort()  # 先排序

        def backtrack(candidates, target, start_index, sum):
            # candidates 从中选择数字
            # 当前的 组合数
            # sum 为当前的和
            if sum == target:
                res.append(path[:])
            if sum > target:
                return  # 剪枝
            for i in range(start_index, len(candidates)):
                if sum + candidates[i] > target:
                    return
                sum = sum + candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, i, sum)
                sum -= candidates[i]
                path.pop()

        backtrack(candidates, target, 0, 0)
        return res

sol = Solution()
condidates = [2,3,6,7]

target = 5
print(sol.combinationSum(condidates, target))

class Solution:
    def subsets(self, nums):
        res = []

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         res.append(nums[i:j+1])
        # return res
        # for i in range(len(nums)):
        #     if res == []:
        #         res.append([nums[i]])
        #     else:
        #         for j in range(len(res)):
        #             tmp = res[j][:]
        #             tmp.append(nums[i])
        #             res.append(tmp)
        #         res.append([nums[i]])
        # return res
        res = []
        path = []

        def backtrack(k, start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, len(nums)):  # i为nums中的数字的索引
                path.append(nums[i])
                backtrack(k, i + 1)
                path.pop()

        for k in range(len(nums)):
            backtrack(k, 0)
        return res
sol = Solution()
print(sol.subsets([1, 2, 3]))

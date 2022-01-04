# -*- coding: utf-8 -*-
# @Time : 2022/1/4 15:40
# @Author : XDD
# @File : 2122.还原原数组.py
class Solution:
    def recoverArray(self, nums):
        n = len(nums)  # 2*n
        nums.sort()  # 从小到大排序
        for i in range(1, n):
            # 寻找可能的k
            if nums[i] == nums[0] or (nums[i] - nums[0]) % 2 != 0:
                continue

            # 此时找到一个合适 的k
            k = (nums[i] - nums[0]) // 2
            ans = [nums[0] + k]
            visited = [False] * n  # 标注该值是否访问过
            visited[0] = visited[i] = True

            l, r = 0, i
            for j in range(1, n // 2):
                while visited[l]:
                    l += 1
                while r < n and (visited[r] or nums[r] != nums[l] + 2 * k):
                    r += 1

                # 此时，又找到一对
                if r == n:
                    break
                ans.append(nums[l] + k)
                visited[l] = visited[r] = True
            if len(ans) == n // 2:
                return ans
        return None

sol = Solution()
nums = [2,10,6,4,8,12]
print(sol.recoverArray(nums=nums))

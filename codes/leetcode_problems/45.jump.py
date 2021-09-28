class Solution:
    def jump(self, nums):
        # 贪心
        """
                n 长度
                step 步长
                left ，right  当前位置元素能到达的第一个元素和最后一个元素
                cur 当前位置的元素
                """
        n = len(nums)
        step = 0
        left, right, cur = 0, 0, 0

        # 1. 当元素个数为1 直接返回
        if len(nums) == 1:
            return 0

        # 2. 循环
        while left < n:
            # 1. 每次更新当前元素的 left， right
            left = right + 1
            right = cur + nums[cur]

            # 4. 如果 right 值大于 n-1了，说明下一步一定能到，返回
            if right >= n - 1:
                return step + 1

            # 2. 根据贪心算法，找到能走的最远的 下一个元素
            temp = 0
            for i in range(left, right + 1):
                if i + nums[i] > temp:
                    temp = i + nums[i]
                    cur = i

            # 3. 步数加一
            step += 1


sol = Solution()
nums = [3, 2, 1]
print(sol.jump(nums))

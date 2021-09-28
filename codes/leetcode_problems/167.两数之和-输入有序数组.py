nums = [2, 7, 11, 15]
tar = 1


class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)
        p1 = 0
        p2 = n - 1
        if target < numbers[p1] or target > 2 * numbers[p2]:
            return [-1, -1]
        while p1 < p2:
            temp = numbers[p1] + numbers[p2]
            if temp < target:
                p1 += 1
            elif temp > target:
                p2 -= 1
            else:
                return [p1 + 1, p2 + 1]
        return [-1, -1]


s =Solution()
s.twoSum(nums, tar)

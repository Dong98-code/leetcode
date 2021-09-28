class Solution:
    def isHappy(self, n: int) -> bool:
        hash_list = []
        while n != 1:

            sum = 0
            while n > 0:
                temp = n%10
                sum += temp*temp
                n //= 10
            n = sum
            if n in hash_list:
                return False
            hash_list.append(n)

        return True

s = Solution()
s.isHappy(7)

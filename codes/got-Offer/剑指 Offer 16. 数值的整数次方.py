"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。


"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            ret = self.myPow(x, n >> 1)
            ret *= ret
            if n & 1 == 1:
                ret *= x
            return ret

        if x == 0 and n < 0:
            raise ZeroDivisionError
        ret = power(x, abs(n))
        if n < 0:
            return 1.0 / ret
        else:
            return ret

solu = Solution()
print(solu.myPow(x=2,n=10))

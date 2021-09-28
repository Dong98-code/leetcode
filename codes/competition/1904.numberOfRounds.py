class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        # 转换成 分钟数
        t0 = int(startTime[:2]) * 60 + int(startTime[3:])
        t1 = int(finishTime[:2]) * 60 + int(finishTime[3:])
        if t0 > t1:
            t1 += 1440
        t1 = t1 // 15 * 15
        return max(t1 - t0, 0) // 15

sol = Solution()
T1 = "12:01"
T2 = "12:44"
print(sol.numberOfRounds(T1,T2))




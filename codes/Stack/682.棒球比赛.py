class Solution:
    def calPoints(self, ops) -> int:
        s = []
        for sym in ops:
            for sym in ops:
                if sym == 'C':
                    s.pop()
                elif sym == 'D':
                    s.append(2 * s[-1])
                elif sym == '+':
                    s.append(s[-1] + s[-2])
                else:
                    s.append(int(sym))
            return sum(s)
if __name__ == "__main__":
    s = Solution()
    str_list =  ["5","-2","4","C","D","9","+","+"]
    s.calPoints(str_list)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [1]
        for i in range(1, rowIndex + 1):
            ietm = out[i - 1] * (rowIndex - i + 1) / i
            out.append(int(ietm))

        return out

"""
n行m列 =Cnm
Cnm =cnm-1*(n-m+1)/m
"""

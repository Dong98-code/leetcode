# -*- coding: utf-8 -*-
# @Time : 2022/1/1 16:02
# @Author : XDD
# @File : 1044.最长重复子串.py
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = int(1e18 + 7)
        base = 233
        def get_hash_code(L):
            # l 为子串的长度
            hash_code = 0
            x = base**l % MOD
            seen = set()
            for i in range(len(s)):
                if i < L:
                    hash_code = (hash_code * base + ord(s[i])) % MOD
                else:
                    hash_code = (hash_code*base + ord(s[i]) - ord(s[i-l])*x) % MOD
                if hash_code in seen:
                    return True, s[i-L+1:i+1]
                if i >= L-1:
                    seen.add(hash_code)
            return False, '_'
        l, r = 0, len(s)
        ans = ""
        while l < r:
            mid = (1+r+1) >> 1
            ret, tmp = get_hash_code(mid)
            if ret:
                ans =tmp
            if not ret:
                r = mid - 1
            else:
                l = mid
        return ans


sol = Solution()
print(sol.longestDupSubstring("banana"))

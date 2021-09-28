class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # def helper(string):
        #     hash_lst = [0]*10
        #     for letter in string:
        #         index = ord(letter) - ord("a")
        #         hash_lst[index] += 1
        #     cnt = 0 # 用于记录奇数字母的个数
        #     for i in range(len(hash_lst)):
        #         if hash_lst[i] % 2 == 1:
        #             cnt += 1
        #         else:
        #             continue
        #     if cnt <= 1:
        #         return True
        #     else:
        #         return False
        # # l, r左右指针，遍历word
        # num = 0
        # for l in range(len(word)):
        #     for r in range(l, len(word)):
        #         string_tmp = word[l:r+1]
        #         if helper(string_tmp):
        #             num += 1
        # return num
        res = 0
        n = len(word)
        freq = [0] * (1 << 10)
        freq[0] += 1
        state = 0
        for i in range(n):
            offset = ord(word[i]) - ord("a")
            state = state ^ (1 << offset)
            res += freq[state]
            for j in range(10):
                prev = state ^ (1 << j)
                res += freq[prev]
            freq[state] += 1
        return res
sol = Solution()
print(sol.wonderfulSubstrings('aabb'))

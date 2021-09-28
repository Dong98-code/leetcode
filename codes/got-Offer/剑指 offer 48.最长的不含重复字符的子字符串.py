import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # queue = collections.deque()
        # cnt = 0
        # max_len = 0
        # for item in s:
        #     if item not in queue:
        #         queue.append(item)
        #         cnt += 1
        #     else:
        #         while item in queue:
        #             queue.popleft()
        #             cnt -=1
        #         queue.append(item)
        #         cnt += 1
        #     max_len = max(cnt, max_len)
        # return max_len
        dic = {}  # 用字典构造哈希表
        res = 0  # 遍历过程中的最大长度
        i = -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j-i)
        return res

string ="pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(string))

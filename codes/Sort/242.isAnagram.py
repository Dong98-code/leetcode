class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        s_set = set(s)
        t_set = set(t)
        for i in s_set:
            if i not in t_set:
                return False
            else:
                s_count = s.count(i)
                t_count = t.count(i)
                if s_count != t_count:
                    return False
            return True

if __name__ == "__main__":
    solution = Solution()
    s = 'rat'
    t = 'car'
    print(solution.isAnagram(s, t))

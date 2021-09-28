# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         list1 = []
#         for index, item in enumerate(s):
#             if item.isalnum():
#                 if item.isalpha:
#                     list1.append(item.upper())
#                 else:
#                     list1.append(item)
#         list2 = list1[::-1]
#         return list2==list1

"""
双指针
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string1 = ''.join (item.lower() for item in s if item.isalnum())
        length = len(s)
        left = 0
        right = length-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

string = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(string))





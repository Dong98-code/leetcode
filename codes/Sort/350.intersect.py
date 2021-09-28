"""
给定两个数组，编写一个函数来计算它们的交集。
"""
class Solution:
    def intersect(self, nums1, nums2):
        ans = []
        nums2.sort()
        nums1.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        p1 = p2 = 0
        while p1 < l1 and p2 < l2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif  nums1[p1] > nums2[p2]:
                p2 += 1
        else:
            ans.append(nums2[p2])
            p1 += 1
            p2 += 1

        return ans


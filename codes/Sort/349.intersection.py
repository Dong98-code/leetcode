"""
给定两个数组，编写一个函数来计算它们的交集。


"""
class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]




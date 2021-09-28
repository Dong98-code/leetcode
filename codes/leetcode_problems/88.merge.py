class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        i2 = n - 1
        index = m + n -1
        while i1 > 0 or i2 >= -1:
            if i1 == -1:
                nums1[index] = nums2[i2]
                i2 -= 1
            elif i2 == -1:
                nums1[index] = nums1[i1]
                i1 -= 1
            else:
                if  nums1[i1] >= nums2[i2]:
                    nums1[index] = nums1[i1]
                    i1 -= 1

                else:
                    nums1[index] = nums2[i2]
                    i2 -= 1
            index -= 1

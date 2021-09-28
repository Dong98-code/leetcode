class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # dict = {}
        # output = []
        # for i in range(len(nums2)):
        #     dict[nums2[i]] = -1 # 默认值为-1
        #     j = i+1
        #     while j < len(nums2) and nums2[j] <= nums2[i]:
        #         j += 1
        #     if j == len(nums2):
        #         continue
        #     else:
        #         dict[nums2[i]] = nums2[j]
        # for item in nums1:
        #     output.append(dict[item])
        # return output
        d = {}  # 字典
        ans = []
        stack = []
        for item in nums2:
            # dict[nums2[i]] = -1 # 默认值为-1
            # j = i+1
            # while j < len(nums2) and nums2[j] <= nums2[i]:
            #     j += 1
            # if j == len(nums2):
            #     continue
            # else:
            #     dict[nums2[i]] = nums2[j]
            while stack and stack[-1]<item:
                    d[stack.pop()] = item
            stack.append(item)

        for item in nums1:
            ans.append(d.get(item, -1))
        return ans


if __name__ == "__main__":
    s =Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    s.nextGreaterElement(nums1,nums2)

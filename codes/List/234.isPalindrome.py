"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from codes.utils.single_list import *

head = creat_single_list([1,2,2,1])
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # lst1 = []
        # while head:
        #     lst1.append(head.val)
        #     head = head.next
        # return lst1 == lst1[::-1]
        # pre_s, slow, fast = None, copy.copy(head), copy.copy(head)
        pre_s, slow, fast = None, head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            t1 = slow.next
            slow.next = pre_s
            pre_s = slow
            slow = t1

        if fast.next:
            t = slow.next
            slow.next = pre_s
            while slow and t:
                if slow.val == t.val:
                    slow = slow.next
                    t = t.next
                else:
                    return False
            return True
        else:
            t = slow.next
            while pre_s and t:
                if pre_s.val == t.val:
                    pre_s = pre_s.next
                    t = t.next
                else:
                    return False
            return True

sol = Solution()
print(sol.isPalindrome(head))

from codes.utils.single_list import *
head = creat_single_list([1,2,3,4,5])
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head:
            return head
        pre = None
        cur = head
        while cur.next:
            t1 = cur.next
            cur.next = pre
            pre = cur
            cur = t1
        cur.next = pre
        return cur

sol = Solution()
print(sol.reverseList(head))

from codes.utils.single_list import creat_single_list
nums = [1,2,6,3,4,5,6]
head = creat_single_list(nums)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        res = ListNode()
        cur = res
        while head:
            while head and head.val == val:
                head = head.next
            cur.next = head
            cur = cur.next
            if head:
                head = head.next
        return res.next

sol = Solution()
print(sol.removeElements(head, 6))

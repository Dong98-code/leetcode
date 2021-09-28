"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。


"""
from codes.utils.single_list import *
nums = [1,2,6,3,4,5,6]
head = creat_single_list(nums)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return []
        pre = ListNode()
        pre.next = head
        p = pre

        while p:
            if p.next and p.val == val:
                p.next = p.next.next
                p = p.next
            else:
                p = p.next
        return pre.next

sol = Solution()
print(sol.removeElements(head, 6))


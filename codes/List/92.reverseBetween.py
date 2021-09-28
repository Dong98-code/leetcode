"""
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""
from codes.utils.single_list import *
from codes.utils.draw_list import *
head = creat_single_list([1, 2, 3, 4, 5])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = ListNode(0, head)
        pre = dummy_head
        cnt = 1
        while cnt < left:
            cnt += 1
            pre = pre.next
        cur = pre.next

        while cnt < right:
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node
            cnt += 1

        return dummy_head.next

sol = Solution()
draw(sol.reverseBetween(head, 2, 4))







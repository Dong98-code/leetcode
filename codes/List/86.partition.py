"""
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
"""
from codes.utils.single_list import *
from codes.utils.draw_list import *

head = creat_single_list([1])


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        min = ListNode()  # 新建一个list,存放小于x的节点
        cur_min = min
        dummy_head = ListNode(0, head)
        cur = dummy_head
        while cur.next:
            node = cur.next
            if node.val < x:
                cur_min.next = node
                cur_min = cur_min.next
                cur.next = cur.next.next  # 删除小于x的节点

            else:
                cur = cur.next
        if cur.val < x:
            cur_min.next = cur
            cur_min = cur_min.next
        cur_min.next = dummy_head.next  # 连接小链表和大链表
        return min.next


sol = Solution()
draw(sol.partition(head, 2))

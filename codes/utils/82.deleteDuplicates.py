"""
82. 删除排序链表中的重复元素 II
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。
"""
from codes.utils.single_list import *

head = creat_single_list([3,3,3,4,5])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        pre = dummy_head  # 虚拟节点
        while pre.next and pre.next.next:  # 用于判定list中的节点的值 记录遍历
            node1 = pre.next
            node2 = pre.next.next
            if node2.val == node1.val:  # 如果遇到相等的点，则继续往下寻找，知道找到不是的值
                while node2 and (node2.val == node1.val):
                    node2 = node2.next
                pre.next = node2
            else:
                pre = pre.next

        return dummy_head.next

sol = Solution()
print(sol.deleteDuplicates(head))

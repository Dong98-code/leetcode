"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
"""
from codes.utils.single_list import *
from codes.utils.draw_list import *
head = creat_single_list([1, 2, 3, 4, 5])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt += 1
        #  遍历一次，最终结果为
        num = k % cnt
        if num == 0:
            return head
        right = left = head
        for _ in range(num):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        out = left.next
        left.next = None
        cur = out
        while cur.next:
            cur = cur.next
        cur.next = head

        return out
sol = Solution()

draw(sol.rotateRight(head, 16))

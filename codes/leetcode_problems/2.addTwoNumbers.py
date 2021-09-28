"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from codes.utils.single_list import *
from codes.utils.draw_list import *

l1 = creat_single_list([9,9,9,9,9,9,9])
l2 = creat_single_list([9,9,9,9])
# draw(l1)
# draw(l2)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = cur =  ListNode(0)
        # ans = ListNode(0)
        carrying = 0
        while l1 and l2:
            temp = ListNode(0)
            temp.val = l1.val + l2.val+carrying
            carrying = temp.val // 10
            temp.val = temp.val % 10
            l1 = l1.next
            l2 = l2.next
            cur.next = temp
            cur = cur.next
            draw(head)
        # if l1:
        #     temp = ListNode(0)
        #     ans.
        if l1:
            while l1:
                temp = ListNode(0)
                temp.val = l1.val+carrying
                carrying = temp.val // 10
                temp.val = temp.val % 10
                l1 = l1.next
                cur.next = temp
                cur = cur.next
                draw(head)

        if l2:
            while l2:
                temp = ListNode(0)
                temp.val = l2.val + carrying
                carrying = temp.val // 10
                temp.val = temp.val % 10
                l2 = l2.next
                cur.next = temp
                cur = cur.next
                draw(head)
        if carrying:
            temp = ListNode(0)
            temp.val = carrying
            cur.next = temp
            draw(head)

        return head.next



        # return head.next

sol = Solution()
print(sol.addTwoNumbers(l1, l2))



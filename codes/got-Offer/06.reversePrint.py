"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        if not head: # 空结点 直接返回【】
            return []
        ans = []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        while res:
            ans.append(res.pop())
        return ans


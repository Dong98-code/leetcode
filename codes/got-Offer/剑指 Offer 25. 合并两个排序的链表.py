"""
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


def list2chain(l):
    dummy = ListNode()
    h = dummy
    for num in l:
        h.next = ListNode(num)
        h = h.next
    return dummy.next


l1 = list2chain([1, 2, 3,4])
l2 = list2chain([1, 2, 4])




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        pre= ListNode(0)
        pre_node = pre
        while l1 and l2:
            if l1.val < l2.val:
                pre_node.next = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                l2 = l2.next
            pre_node = pre_node.next
            pre_node.next = l1 if l1 else l2
        return pre_node.next
sol = Solution()
print(sol.mergeTwoLists(l1,l2))

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""





def reverseList(head):
    if not head or not head.next:
            return head
    pre, cur=head, head.next
    cur_reverse=reverseList(cur)
    cur.next=pre
    pre.next=None # python 赋值 是 x,y指向同一块内存，一个数值改变，之后的数值也会改变
    return cur_reverse

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __str__(self):
    #     if not self:
    #         return ''
    #     ans = ''
    #     node = self
    #     while node:
    #         ans += str(node.val) + ' '
    #         node = node.next
    #     return ans


def list2chain(l):
    dummy = ListNode()
    h = dummy
    for num in l:
        h.next = ListNode(num)
        h = h.next
    return dummy.next


head = list2chain([1, 2, 3, 4, 5])
node = reverseList(head)
print(node)

"""
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from codes.utils.single_list import creat_single_list
from codes.utils.draw_list import draw
list_a = [2, 6, 4]
list_b = [1, 5]
list_A = creat_single_list(list_a)
list_B = creat_single_list(list_b)
draw(list_A)
draw(list_B)



class Solution:
    def getIntersectionNode(self, headA, headB):
        pa = headA
        pb = headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

s = Solution()
s.getIntersectionNode(list_A, list_B)



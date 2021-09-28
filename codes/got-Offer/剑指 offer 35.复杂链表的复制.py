# coding=utf-8
"""
复杂链表的复制
链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
分为三步完成：
一复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
二为每个新结点设置other指针
三把复制后的结点链表拆开
"""
import random


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 赋值链表
        # if not head:
        #     return head
        # cur = head
        # # 赋值原来的链表，但是random没有链接
        # # 将head 赋值给cur,此时cur与head 共享同一个地址，cur，改变head也改变
        # while cur:
        #     tmp = Node(cur.val)
        #     tmp.next = cur.next
        #     cur.next = tmp
        #     cur = tmp.next
        # print_nodes(head)
        # # 现在head 和cur 都是复制好的Nodelist
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next  # 中间隔着复制的node
        # # 拆开
        # print_nodes(head)
        # cur = res = head.next
        # pre = head
        # while cur.next:
        #     pre.next = pre.next.next
        #     cur.next = cur.next.next
        #     pre = pre.next
        #     cur = cur.next
        # pre.next = None # 单独处理原链表尾节点
        # return res
        if not head:
            return head
        cur = head
        dic = {}
        while cur:
            node = Node(cur.val)
            dic[cur] = node
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]

def print_nodes(head):
    # 打印结点值，结点other的值，用来比较
    ret = []
    while head:
        tmp = [head.val]
        if head.random:
            tmp.append(head.random.val)
        ret.append(tmp)
        head = head.next
    print (ret)




def construct_nodes(vals):
    if not vals:
        return Node
    move = head = Node(vals.pop(0))
    nodes = [None, head]
    for v in vals:
        tmp = Node(v)
        move.next = tmp
        nodes.append(tmp)
        move = move.next
        # print [node.val for node in nodes if node]
    move = head
    while move:
            # 设置other指针为随机结点
        move.random = random.choice(nodes)
        move = move.next
    return head


if __name__ == '__main__':
    link = construct_nodes([1, 2, 3, 4, 5])
    print_nodes(link)
    sol = Solution()
    print_nodes(sol.copyRandomList(link))

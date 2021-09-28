
class Node(object):
    """节点"""

    def __init__(self, val):
        self.val = val
        self.next = None  # 初始设置下一节点为空


def creat_single_list(nums):
    if nums[0] is None:
        return None
    head = Node(nums[0])
    nodes = [head]
    j = 1
    for node in nodes:
        if node is not None:
            node.next = (Node(nums[j]) if nums[j] is not None else None)
            nodes.append(node.next)
            j += 1
            if j == len(nums):
                return head

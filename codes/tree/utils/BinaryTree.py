class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
# 建立二叉树是以层序遍历方式输入，节点不存在时以 'None' 表示


def creat_tree(node_list):
    if node_list[0] is None:
        return None
    root = TreeNode(node_list[0])
    # 根节点
    nodes = [root]
    # 节点的列表,
    j = 1
    for node in nodes:
        if node is not None:
            node.left = (TreeNode(node_list[j]) if node_list[j] is not None else None)
            nodes.append(node.left)
            j += 1
            if j == len(node_list):
                return root
            node.right = (TreeNode(node_list[j])if node_list[j] is not None else None)
            j += 1
            nodes.append(node.right)
            if j == len(node_list):
                return root


# if __name__ == "__main__":
#     list = [1,2,None]
#     creat_tree(list)

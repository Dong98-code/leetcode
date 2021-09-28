import networkx as nx
import matplotlib.pyplot as plt

# def create_graph(G, node, pos={}, x=0, y=0, layer =1):
#     pos[node.val] = (x, y)
#     #  pos为一个字典，key存放node的key, value为坐标对
#     if node.left:  # 存在左子树
#         G.add_edge(node.val, node.left.val)
#         l_x, l_y = x - 1/2**layer, y-1
#         l_layer = layer+1
#         create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
#     if node.right:
#         G.add_edge(node.val, node.right.val)
#         r_x, r_y = x+1/2**layer, y-1
#         r_layer = layer+1
#         create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
#
#     return (G, pos)
#
#
# def draw_graph(node):
#     graph = nx.DiGraph()
#     graph, pos = create_graph(graph, node)
#     fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
#     nx.draw_networkx(graph, pos, ax=ax, node_size=1000, alpha = 0.5)
#     plt.show()

from collections import defaultdict


def draw(node):   # 以某个节点为根画图
    saw = defaultdict(int)

    def create_graph(G, node, p_name, pos = {}, x=0, y=0, layer=1):
        if node is None:
            return
        name = str(node.val)
        saw[name] += 1
        if name in saw.keys():
            name += ' '* saw[name]

        G.add_edge(p_name, name)
        pos[name] = (x, y)

        l_x, l_y = x - 1/2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, name, x=l_x, y=l_y, pos=pos, layer=l_layer)

        r_x, r_y = x + 1/2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right,name, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node,"     ")
    pos["     "] = (0,0)
    fig, ax = plt.subplots(figsize=(10, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=3000, alpha = 0.5, node_color ='yellow', font_size =25)
    plt.show()



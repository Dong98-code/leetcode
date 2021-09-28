import networkx as nx
import matplotlib.pyplot as plt
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

        n_x, n_y = x+1, y
        l_layer = layer + 1
        create_graph(G, node.next, name, x=n_x, y=n_y, pos=pos, layer=l_layer)

        # r_x, r_y = x + 1/2 ** layer, y - 1
        # r_layer = layer + 1
        # create_graph(G, node.right,name, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node,"     ")
    pos["     "] = (0,0)
    fig, ax = plt.subplots(figsize=(10, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=3000, alpha = 0.5, node_color ='yellow', font_size =25)
    plt.show()
#
# list_a = [2, 6, 4]
# list_b = [1, 5]
# list_A = creat_single_list(list_a)
# list_B = creat_single_list(list_b)
# draw(list_A)



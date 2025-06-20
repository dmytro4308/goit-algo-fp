import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Step 1: Traverse the tree and collect values
def collect_values(root):
    values = []
    def inorder(node):
        if node:
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
    inorder(root)
    return values

# Step 2: Build binary heap from sorted values (min-heap)
def build_heap_from_values(values):
    nodes = [Node(val) for val in values]
    for i in range(len(nodes)):
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < len(nodes):
            nodes[i].left = nodes[left_i]
        if right_i < len(nodes):
            nodes[i].right = nodes[right_i]
    return nodes[0] if nodes else None

# Main function to convert tree to heap
def convert_to_heap(root):
    values = collect_values(root)
    values.sort()  # For min-heap
    return build_heap_from_values(values)

# Original tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Convert to heap and draw
heap_root = convert_to_heap(root)
draw_tree(heap_root)

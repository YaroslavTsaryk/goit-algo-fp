import uuid
import heapq
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root,title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(title,figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def addnodes(node,id,lst):
    left_id = 2 * id + 1
    right_id = 2 * id + 2
    if left_id < len(lst):
        node.left = Node(lst[left_id])
        addnodes(node.left,left_id,lst)
    if right_id < len(lst):
        node.right = Node(lst[right_id])
        addnodes(node.right,right_id,lst)
        

# Створення купи
#data = [4, 1, 14, 2, 3, 11, 3, 7, 10, 20]
data = [0, 4, 1, 5, 10, 3 ]
heapq.heapify(data)
print(data)

root = Node(data[0])

# Створення дерева
addnodes(root,0,data)

step=0
def dfs_recursive(root, visited=None):
    global step
    if visited is None:
        visited = set()
    visited.add(root)
    root.color=f"#{(hex(12+step*20)).replace("0x","").zfill(2)}{(hex(96+step*5)).replace("0x","").zfill(2)}F0"
    step+=1
        
    if root.left not in visited and root.left != None:
        dfs_recursive(root.left, visited)
    if root.right not in visited and root.right != None:
        dfs_recursive(root.right, visited)


dfs_recursive(root)
        
draw_tree(root,"DFS")


step = 0
def bfs_recursive(queue, visited=None):
    global step
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    if vertex:
        # Перевіряємо, чи відвідували раніше дану вершину
        if vertex not in visited:
            # Якщо не відвідували, міняємо колір            
            vertex.color=f"#{(hex(12+step*20)).replace("0x","").zfill(2)}{(hex(96+step*5)).replace("0x","").zfill(2)}F0"
            step+=1
            # Додаємо вершину до множини відвіданих вершин.
            visited.add(vertex)
            # Додаємо невідвіданих сусідів даної вершини в кінець черги.
            queue.extend(set([vertex.left,vertex.right]) - visited)
        # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
        bfs_recursive(queue, visited)
    
bfs_recursive(deque([root]))
draw_tree(root,"BFS")
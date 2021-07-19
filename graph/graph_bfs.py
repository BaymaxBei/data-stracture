from typing import List
import numpy as np
from graph_stracture import Node, Edge, Graph, generate_random_graph_matrix, createGraphByMatrix

def graph_bfs(node: Node) -> List:
    if node is None:
        return None
    res = []
    node_queue = []
    node_set = set()
    node_queue.append(node)
    node_set.add(node)
    while node_queue:
        node = node_queue.pop(0)
        res.append(node.value)
        for next_node in node.nexts:
            if next_node not in node_set:
                node_queue.append(next_node)
                node_set.add(next_node)
    return res

def graph_dfs(node: Node) -> List:
    if node is None:
        return None
    res = []
    stack = []
    res.append(node)
    stack.append(node)
    while stack:
        node = stack.pop(-1)
        for next in node.nexts:
            if next not in res:
                res.append(next)
                stack.append(node)
                stack.append(next)
                break
    return res

def graph_topology(graph):
    res = []
    inmap = {}
    zeroinnode = []
    for value, node in graph.nodes.items():
        inmap[node] = node.in_num
        if node.in_num==0:
            zeroinnode.append(node)
    while zeroinnode:
        node = zeroinnode.pop(0)
        res.append(node)
        for next in node.nexts:
            inmap[next] -= 1
            if inmap[next]==0:
                zeroinnode.append(next)
    return res

if __name__ == '__main__':
    # matrix = generate_random_graph_matrix()
    matrix = [[ 0,  9, -1, -1, -1,  2,  7, -1],
 [-1,  0, -1,  7, -1, -1, -1,  9],
 [ 2, 10,  0, -1, -1, -1,  7, -1],
 [-1, -1,  3,  0,  4, -1,  4,  7],
 [-1, -1,  6,  4,  0,  1, 10, -1],
 [ 3, -1, -1, -1,  7,  0,  7, -1],
 [-1,  7, -1, -1, -1, -1,  0, -1],
 [-1, -1,  7, -1, -1,  5,  7,  0]]
    
    matrix = [[ 0,  9, -1, -1, -1,  2,  7, -1],
 [-1,  0, -1,  7, -1, -1, -1,  9],
 [-1, -1,  0, -1, -1, -1,  7, -1],
 [-1, -1,  3,  0,  -1, -1,  4,  7],
 [-1, -1,  6,  4,  0,  1, 10, -1],
 [-1, -1, -1, -1,  -1,  0,  7, -1],
 [-1, -1, -1, -1, -1, -1,  0, -1],
 [-1, -1,  7, -1, -1,  5,  7,  0]]
    matrix = np.array(matrix)
    graph = createGraphByMatrix(matrix)
    print(matrix)
    # res = graph_bfs(graph.nodes[0])
    # res = graph_dfs(graph.nodes[0])
    res = graph_topology(graph=graph)
    print(res)
    for node in res:
        print(node.value)
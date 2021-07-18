from typing import List
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

if __name__ == '__main__':
    matrix = generate_random_graph_matrix()
    graph = createGraphByMatrix(matrix)
    print(matrix)
    res = graph_bfs(graph.nodes[0])
    print(res)
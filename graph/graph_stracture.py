import numpy as np

# 图的表示方法

# 邻接表法
'''
A: (C, 3), (D, 4)
B: ...
C: ...
D: ...
'''

# 邻接矩阵法
'''
    A   B   C   D
A   0   2   inf 1
B   3   0   4   inf
C   1   2   0   7
D   4   inf 2   0

'''

# 三元组表示法
'''
[权重, 出发点, 到达点]
[
    [3, 1, 2]
    [4, 2, 3]
    [9, 1, 3]
]
'''

# 王牌表示法：节点、边表示法
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.in_num = 0
        self.out_num = 0
        self.nexts = []
        self.edges = []

class Edge:
    def __init__(self, weight, from_node, to_node) -> None:
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []

def createGraphByMatrix(matrix):
    '''
    将图的邻接矩阵转化为王牌表示
    '''
    graph = Graph()
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if i!=j and matrix[i][j]!=-1:
                if i not in graph.nodes:
                    graph.nodes[i] = Node(i)
                if j not in graph.nodes:
                    graph.nodes[j] = Node(j)
                graph.nodes[i].out_num += 1
                graph.nodes[j].in_num += 1
                graph.nodes[i].nexts.append(graph.nodes[j])
                edge = Edge(matrix[i][j], graph.nodes[i], graph.nodes[j])
                graph.nodes[i].edges.append(edge)
                graph.edges.append(edge)
    return graph

def generate_random_graph_matrix(n=8, w=20):
    '''
    随机生成图的邻接矩阵表示，n为矩阵的维度，w为图中边的权重最大值（权重范围：从1到w）
    '''
    matrix = np.random.randint(0, w, size=(n, n))
    value_arr = [-1]*int(w/2)
    value_arr.extend(list(range(1, w-int(w/2)+1)))
    for i in range(n):
        for j in range(n):
            if i==j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = value_arr[matrix[i][j]]
    return matrix

def createGraphByTriTuple(trituple):
    graph = Graph()
    for tri in trituple:
        weight = tri[0]
        fromnode = tri[1]
        tonode = tri[2]
        if fromnode not in graph.nodes:
            graph.nodes[fromnode] = Node(fromnode)
        if tonode not in graph.nodes:
            graph.nodes[tonode] = Node(tonode)
        graph.nodes[fromnode].out_num += 1
        graph.nodes[tonode].in_num += 1
        graph.nodes[fromnode].nexts.append(graph.nodes[tonode])
        weight = Edge(weight, graph.nodes[fromnode], graph.nodes[tonode])
        graph.nodes[fromnode].edges.append(weight)
        graph.edges.append(weight)
    return graph

def matrixToTriTuple(matrix):
    trituple = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            weight = matrix[i][j]
            if weight not in (0, -1):
                trituple.append([weight, i, j])
    return trituple

def isSameGraph(graph1, graph2):
    assert graph1.nodes.__len__()==graph2.nodes.__len__()
    assert len(graph1.edges)==len(graph2.edges)
    for k, v in graph1.nodes.items():
        assert v.value==graph2.nodes[k].value
        assert v.in_num==graph2.nodes[k].in_num
        assert v.out_num==graph2.nodes[k].out_num
        assert len(v.nexts)==len(graph2.nodes[k].nexts)
        assert len(v.edges)==len(graph2.nodes[k].edges)

    graph2_edges = graph2.edges
    for i, edge in enumerate(graph1.edges):
        assert edge.weight==graph2_edges[i].weight
        assert edge.from_node.value==graph2_edges[i].from_node.value
        assert edge.to_node.value==graph2_edges[i].to_node.value



if __name__ == '__main__':
    matrix = generate_random_graph_matrix()
    print(matrix)


    trituple = matrixToTriTuple(matrix)
    print(trituple)

    graph1 = createGraphByMatrix(matrix=matrix)
    graph2 = createGraphByTriTuple(trituple=trituple)
    isSameGraph(graph1, graph2)

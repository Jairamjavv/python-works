# Denoted by G(V,E) => Graph(Vertices, Edges)
# Vertices are Nodes/vertexes
# Edges are lines connecting Nodes

# Graph using Adjacency matrix
class Graph():
    def __init__(self, nodes: int, edges: int):
        # create an empty nodesxnodes matrix
        self.mat = []
        for i in range(nodes):
            self.mat.append([])
            for j in range(nodes):
                self.mat[i].append(0)
        self.nodes = nodes
        self.edges = edges

    def print_graph(self):
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(self.mat[i][j], end="")
            print()

    def add_edge(self, edge: tuple[int, int]):
        a, b = edge
        self.mat[a][b] = 1
        self.mat[b][a] = 1

    def bfs(self):
        pass

graph = Graph(4, 0)
graph.add_edge((1,2))
graph.add_edge((1,3))
graph.add_edge((2,3))
graph.print_graph()
    
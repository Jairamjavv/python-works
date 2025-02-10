class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    def addNeighbour(self, neighbour, G):
        G.addEdge(self.id, neighbour)

    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def getVertexId(self):
        return self.id
    
    def setVertexId(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            # Creating a new vertex.
            newVertex = Vertex(i)
            # Storing the created vertex as a list.
            self.vertices.append(newVertex)

    def setVertex(self, vertex, id):
        if 0 <= vertex < self.numVertices:
            self.vertices[vertex].setVertexId(id)

    def getVertex(self, n):
        for vertex in range(0, self.numVertices):
            if n == self.vertices[vertex].getVertexId():
                return vertex
        return -1
            
    def addEdge(self, fromVertex, toVertex, cost = 0):
        if self.getVertex(fromVertex) != -1 and self.getVertex(toVertex) != -1:
            self.adjMatrix[self.getVertex(fromVertex)][self.getVertex(toVertex)] = cost
            # for directed graph don't add the below line
            self.adjMatrix[self.getVertex(toVertex)][self.getVertex(fromVertex)] = cost

    def getVertices(self):
        vertices = []
        for vertex in range(0, self.numVertices):
            vertices.append(self.vertices[vertex].getVertexId())
        return vertices
    
    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    u_id = self.vertices[u].getVertexId()
                    v_id = self.vertices[v].getVertexId()
                    edges.append((u_id, v_id, self.adjMatrix[u][v]))
            return edges
        
if __name__ == '__main__': 
    G = Graph(3)
    G.setVertex(0,'a') 
    G.setVertex(1, 'b') 
    G.setVertex(2, 'c') 
    print ('Graph data:')  
    G.addEdge('a', 'c', 10)   
    G.addEdge('a', 'b', 20) 
    G.addEdge('c', 'b', 30) 
    G.addEdge('b', 'a', 40) 
    print (G.printMatrix())       
    print (G.getEdges())
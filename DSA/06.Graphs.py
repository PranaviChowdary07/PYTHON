class Vertex:
    def __init__(self,key):
        self.key = key
        self.adjacent = {}
        self.visited = False

    def setKey(self,key):
        self.key = key
    def getKey(self):
        return self.key
    
    def getVisited(self):
        return self.visited
    def setVisited(self,val=True):
        self.visited = val

    def addNeighbour(self,neighbour,weight = 0):
        self.adjacent[neighbour] = weight

    def getNeighbour(self):
        return self.adjacent.keys()
    def getWeight(self,neighbour):
        return self.adjacent[neighbour]
    
class Graph:
    # Graph is undirected by default
    def __init__(self,directed = False):
        self.vertices = {}
        self.numberOfVertices = 0
        self.directed =directed

    def addVertex(self,key):
        node = Vertex(key)
        self.vertices[key] = node
        self.numberOfVertices +=1
        return node

    def addEdge(self,frm,to,weight = 0):
        if frm not in self.vertices:
            self.addVertex(frm)

        if to not in self.vertices:
            self.addVertex(to)
        self.vertices[frm].addNeighbour(self.vertices[to],weight)

        if not self.directed:
            self.vertices[to].addNeighbour(self.vertices[frm],weight)
        
    def getVertex(self,key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
        
    def getEdges(self):
        edges = []
        for v in self.vertices:
            edgesFromVertex = []

            for w in self.vertices[v].getNeighbour():
                frm = self.vertices[v].getKey()
                to = w.getKey()
                weight = self.vertices[v].getWeight(w)
                edgesFromVertex.append((frm,to,weight))

            if len(edgesFromVertex)!= 0:
                edges.append(edgesFromVertex)
        return edges
    
if __name__ == '__main__':
    g = Graph(directed=False)
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')
    g.addEdge('A','B',4)
    g.addEdge('B','C',5)
    g.addEdge('C','D',3)
    g.addEdge('D','E',6)
    g.addEdge('D','A',1)
    g.addEdge('E','A',3)
    g.addEdge('F','C',4)
    g.addEdge('D','B',7)
    g.addEdge('D','C',2)
    g.addEdge('F','B',8)

    for edgeSet in g.getEdges():
        print('Edges from',edgeSet[0][0] + ': ',end ="")
        print(edgeSet)


""" 
Output:
Edges from A: [('A', 'B', 4), ('A', 'D', 1), ('A', 'E', 3)]
Edges from B: [('B', 'A', 4), ('B', 'C', 5), ('B', 'D', 7), ('B', 'F', 8)]
Edges from C: [('C', 'B', 5), ('C', 'D', 2), ('C', 'F', 4)]
Edges from D: [('D', 'C', 2), ('D', 'E', 6), ('D', 'A', 1), ('D', 'B', 7)]
Edges from E: [('E', 'D', 6), ('E', 'A', 3)]
Edges from F: [('F', 'C', 4), ('F', 'B', 8)]
 """




                



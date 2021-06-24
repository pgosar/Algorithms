class Graph:
    
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []
    
    def addEdge(self, x, y, weight):
        self.graph.append([x, y, weight])
    
    def print(self, distance):
        print("Vertex Distance from Source")
        
        for i in range(self.vertex):
            print("{0}\t\t{1}".format(i, distance[i]))
    
    def bellmanFord(self, root):
        
        distance = [float("inf")] * self.vertex
        distance[root] = 0
        
        for i in range(self.vertex-1):
            
            for x, y, weight in self.graph:
                if distance[x] != float("inf") and distance[x] + weight < distance[y]:
                    distance[y] = distance[x] + weight
        
        for x, y, weight in self.graph:
            if distance[x] != float("inf") and distance[x] + weight < distance[y]:
                return float('-inf')
        
        self.print(distance)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellmanFord(0)

g2 = Graph(4)
g.addEdge(0,1,1)
g.addEdge(1,2,-1)
g.addEdge(2,3,-1)
g.addEdge(3,0,-1)

g2.bellmanFord(0)
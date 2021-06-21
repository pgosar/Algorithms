#this is an algorithm to find the shortest path in a nonnegative acyclic graph which can be either directed or undirected
#this uses a list to represent the graph. 
import sys

class Graph():
    
    def __init__(self, vertices): #creating the graph
        self.vertex = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
    def print(self, distance):
        print("Vertex \t distance")
        for i in range(self.vertex):
            print(i, "\t", distance[i])
    
    def minDistance(self, distance, set):
        min = sys.maxsize
        
        for i in range(self.vertex): #finds min distance
            if distance[i] < min and set[i] == False:
                min = distance[i]
                index = i
        return index

    def dijkstra(self, root):
        
        distance = [sys.maxsize] * self.vertex #creates list full of max ints for how many vertices there are
        distance[root] =0
        shortest = [False] * self.vertex
        
        for i in range(self.vertex): #finds vertex with minimum distance from the unprocessed vertices
            x = self.minDistance(distance, shortest) 
            shortest[x] = True
            
            for y in range(self.vertex): #if the current distance 
                
                if (self.graph[x][y] > 0 and shortest[y] == False and distance[y] > distance[x] + self.graph[x][y]):     
                    distance[y] = distance[x] + self.graph[x][y]
                    
        self.print(distance)

g = Graph(9)

#this is an adjacency matrix, position 4,5 represents the distance between vertex 4 and 5
#position 2,3 represents distance between 2 and 3 etc.
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11,0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14,0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
  
g.dijkstra(0)


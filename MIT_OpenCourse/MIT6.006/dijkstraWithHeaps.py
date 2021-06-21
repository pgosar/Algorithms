#time complexity: O((e+v)*logv) 
#this is an algorithm to find the shortest path in a nonnegative acyclic graph which can be either directed or undirected
#uses binary heap to lower time complexity from O(v^2)

from collections import defaultdict
import sys

class Heap():
    
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
    
    def minHeap(self, vertex, distance): 
        minHeap = [vertex, distance]
        return minHeap

    def minHeapify(self, index): #heapifies the heap
        smallest = index
        left = 2*index+1
        right = 2*index+2
        
        if left < self.size and self.array[left][1] < self.array[smallest][1]:
             smallest = left
        
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        
        if smallest != index:
            
            self.pos[self.array[smallest][0]] = index
            self.pos[ self.array[index][0]] = smallest
            
            temp = self.array[smallest]
            self.array[smallest] = self.array[index]
            self.array[index] = temp
            
            self.minHeapify(smallest)
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def getMin(self): #gets min node from heap
        
        if self.isEmpty() == True:
            return
        
        root = self.array[0]
        last = self.array[self.size-1]
        self.array[0] = last
        
        self.size -=1
        self.minHeapify(0)
        
        return root
    
    def decreaseKey(self, v, dist): #decreases key of a node, necessary for edge relaxation
 
        i = self.pos[v]
        self.array[i][1] = dist
 #travel through tree while it isnt heapified and swap nodes with its parent
        while i > 0 and self.array[i][1] < self.array[int((i-1)/2)][1]:
 
            self.pos[self.array[i][0]] = int((i-1)/2)
            self.pos[self.array[int((i-1)/2)][0]] = i

            temp = self.array[i]
            self.array[i] = self.array[int((i-1)/2)]
            self.array[int((i-1)/2)] = temp
            
            i = int((i-1)/2)

    def checkMinHeap(self, vertex):
        
        if self.pos[vertex] < self.size:
            return True
        return False

def printArr(dist, n):
    print("Vertex\tDistance")
    for i in range(n):
        print("%d\t\t%d" % (i,dist[i]))
        
class Graph():
    
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)
        
    #adds edge from source to destination with assigned weight
    def addEdge(self, source, destination, weight): 
        
        newNode = [destination, weight]
        self.graph[source].insert(0, newNode)

        #its a undirected graph so it goes both ways
        newNode = [source, weight]
        self.graph[destination].insert(0, newNode)
        
    def dijkstra(self, source):
        
        vertex = self.vertex
        distance = []
        
        newMinHeap = Heap()
        
        for i in range(vertex): #initialize min heap
            distance.append(sys.maxsize)
            newMinHeap.array.append(newMinHeap.minHeap(i, distance[i]))
            newMinHeap.pos.append(i)
            
        #edge relaxation
        newMinHeap.pos[source] = source
        distance[source] = 0
        newMinHeap.decreaseKey(source, distance[source])
        newMinHeap.size = vertex
        
        #goes through all unprocessed nodes, updates distance values, extracts min distance
        while newMinHeap.isEmpty() == False:
            
            heapNode = newMinHeap.getMin()
            x = heapNode[0]
            
            for i in self.graph[x]:
                
                y = i[0]
                if (newMinHeap.checkMinHeap(y) == True and 
                    distance[x] != sys.maxsize and
                    i[1] + distance[x] < distance[y]):

                    distance[y] = i[1] + distance[x]
                    newMinHeap.decreaseKey(y, distance[y])
        
        printArr(distance, vertex)
        
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
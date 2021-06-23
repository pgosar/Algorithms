#breadth first search for a graph, also works for trees 

graph={5:[3,7], 3:[2,4], 7:[8], 2:[], 4:[8], 8:[]}

def bfs(graph, root):
    visited=[]
    queue=[]    
    visited.append(root)
    queue.append(root)
    while queue:
        node = queue.pop(0)
        
        for x in graph[node]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
                
    return visited

print(bfs(graph,5))
print(bfs(graph, 3))
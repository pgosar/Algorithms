graph={5:[3,7], 3:[2,4], 7:[8], 2:[], 4:[8], 8:[]}

def dfs(graph, key, visited):
    
    visited = []
    if key not in visited:
        visited.append(key)
        
        for i in graph[key]:
            visited = dfs(graph, i, visited)
            
    return visited

print(dfs(graph, 5))
print(dfs(graph, 3))
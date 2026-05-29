import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            
            visited.add(v)
            
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():
                
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)
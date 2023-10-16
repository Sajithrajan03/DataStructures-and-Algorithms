from collections import defaultdict, deque

def reachable_stations(graph):
    
    reachable = defaultdict(set)
    
    
    for station in graph:
        visited = set()  
        queue = deque([(station, 0)])  
        
        while queue:
            current, distance = queue.popleft()
            
            if distance > 4:
                continue  
            
            visited.add(current)
            reachable[station].add(current)
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
    
    return reachable


graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6],
    4: [1, 7],
    5: [2],
    6: [3],
    7: [4]
}

result = reachable_stations(graph)


for station, reachable_set in result.items():
    print(f"Station {station} can reach stations: {reachable_set}")

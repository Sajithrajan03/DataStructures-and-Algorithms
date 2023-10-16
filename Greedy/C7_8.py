import heapq

def nasa_problem(graph):
    n = len(graph)
    max_bandwidth = 0
    mst_edges = []

    start_vertex = 0
    mst_vertices = {start_vertex}
    not_mst_vertices = set(range(n))
    not_mst_vertices.remove(start_vertex)
    
    pq = []

    for vertex, bandwidth in enumerate(graph[start_vertex]):
        heapq.heappush(pq, (bandwidth, start_vertex, vertex))

    while len(mst_vertices) < n:
        bandwidth, u, v = heapq.heappop(pq)

        if v in not_mst_vertices:
            max_bandwidth += bandwidth
            mst_edges.append((u, v))
            mst_vertices.add(v)
            not_mst_vertices.remove(v)

            for vertex, bandwidth in enumerate(graph[v]):
                if vertex in not_mst_vertices:
                    heapq.heappush(pq, (bandwidth, v, vertex))

    return max_bandwidth, mst_edges

def main():
    
    
    
    graph = [
        [0, 3, 2, 0],
        [3, 0, 0, 1],
        [2, 0, 0, 4],
        [0, 1, 4, 0]
    ]

    max_bandwidth, mst_edges = nasa_problem(graph)
    print(max_bandwidth)
    for u, v in mst_edges:
        print(u, v)

if _name_ == "_main_":
    main()






class Graph:
    def __init__(self):
        self.graph = {}
    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u]  = [v,]
    def print(self):
        for i in self.graph:
            print(f"{i} -> {self.graph[i]}")
    def BFS(self,v):
        visited =list()
        q = [v,]
        while(len(q)!=0):
            node = q.pop(0)
            if node in visited:
                pass
            else:
                visited.append(node)
                for i in self.graph[node]:
                    q.append(i)
        print(visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.print()
g.BFS(0)
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

    
    def dfstrversal(self,visited,v):
        if v in visited:
            return
        visited.append(v)
        for i in self.graph[v]:
            self.dfstrversal(visited,i)
        
    def DFS(self,v):
        visited = list()
        self.dfstrversal(visited,v)
        print(visited)

g = Graph()
g.graph = {1:[2,3],2:[1,5,6],3:[1,4,7],4:[3,8],5:[2],6:[2],7:[3,8],8:[4,7]}
g.print()
g.DFS(1)
class graph:
    def __init__(self):
        self.graph= list
    def bfs(self,v):
        visited = set()
        queue = [v,]
        while(len(queue)):
            node = queue.pop(0)
            if node in visited:
                pass
            else:
                visited.add(node)
                for i in self.graph[node]:
                    queue.append(i)
        print(visited)

    def DFS(self,v):
        visited = set()
        self.dfstraversal(visited,v)
        print(visited)
    def dfstraversal(self,visited,v):
        if v in visited:
            return 
        visited.add(v)
        for i in self.graph[v]:
            self.dfstraversal(visited,i)

g = graph()
g.graph = {1:[2,3],2:[1,5,6],3:[1,4,7],4:[3,8],5:[2],6:[2],7:[3,8],8:[4,7]}
g.bfs(1)
g.DFS(1)
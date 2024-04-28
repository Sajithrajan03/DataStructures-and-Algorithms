class Graph():
    def __init__(self):
        self.graph = {}
    def addEgde(self,u,v):

        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v,]
    def print(self):
        for i in self.graph:
            print(f'{i} -> {self.graph[i]}')
    def bfs(self,v):
        visit = list()
        q = [v,]
        while (len(q)):
            node = q.pop(0)
            if node in visit:
                pass
            else:
                visit.append(node)
                for i in self.graph[node]:
                    q.append(i)
        print(visit)
    def 

g =  Graph()
g.addEgde(1,2)
g.addEgde(1,3)
g.addEgde(2,1)

g.addEgde(3,1)
g.print()
g.bfs(1)
        


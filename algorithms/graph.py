from collections import deque
import heapq
from typing import *

class Graph:
    def __init__(self):
        self.d = DefaultDict(list)
        self.size = 0

    def sort(self):
        self.d = dict(sorted(self.d.items()))

    def adjacencyList(self):
        adj = [[0]*self.size for _ in range(self.size)]
        for u in self.d:
            if isinstance(self.d[u][0], List):
                for v,weight in self.d[u]:
                    adj[u][v] = weight
            else:
                for v in self.d[u]:
                    adj[u][v] = 1
        for a in adj:
            print(a)

    def exampleUUG():
        g = undirectedUnweightedGraph()
        g.add_edge(1,2)
        g.add_edge(1,0)
        g.add_edge(2,0)
        g.add_edge(2,3)
        g.add_edge(2,4)
        return g

    def exampleUWG():
        g = undirectedWeightedGraph()
        g.add_edge(0,1,4)
        g.add_edge(0,2,8)
        g.add_edge(1,4,6)
        g.add_edge(2,3,2)
        g.add_edge(3,4,10)
        return g

class undirectedGraph(Graph):

    def dfsRec(self,node:int,res:List[int],visited=None):
        if visited is None:
            visited = set()

        visited.add(node)
        res.append(node)

        for child in self.d[node]:
            if isinstance(child, List):
                child = child[0]
            if child not in visited:
                self.dfsRec(child,res,visited)

    def dfs(self,node:int) -> List[int]:
        res = []
        if node not in self.d:
            print(f"Der Startknoten {node} existiert nicht im Graph")
        else:
            res = []
            self.dfsRec(node,res)
        return res

    def bfs(self,node:int) -> List[int]:
        res = []
        visited = {node}
        q = deque([node])
        while q:
            curr = q.popleft()
            res.append(curr)
            for ng in self.d[curr]:
                if isinstance(ng, List):
                    ng = ng[0]
                
                if ng not in visited:
                    q.append(ng)
                    visited.add(ng)
        return res

    def connected(self) -> bool:
        if self.d:
            start = next(iter(self.d))
            allNodes = self.dfs(start)
            if len(allNodes) == self.size:
                return True
            else:
                return False
        else:
            return False

class undirectedUnweightedGraph(undirectedGraph):
    def add_edge(self,u,v):
        self.d[u].append(v)
        self.d[v].append(u)
        self.size += 1

    def printGraph(self):
        if self.d:
            self.sort()
            for k in self.d.keys():
                print(str(k) + ": " + str(self.d[k]))
        else:
            print("Empty")

class undirectedWeightedGraph(undirectedGraph):
    def add_edge(self,u,v,weight):
        self.d[u].append([v,weight])
        self.d[v].append([u,weight])
        self.size += 1

    def printGraph(self):
        if self.d:
            self.sort()
            for v in self.d:
                output = str(v) + ": "
                for node in self.d[v]:
                    output += str(node) + ", "
                print(output[:-2])
        else:
            print("Empty")

    def dijkstraAlgo(self,src):
        pq = []
        dist = [float('inf')]*self.size
        heapq.heappush(pq,[0,src])
        dist[src] = 0

        while pq:
            u = heapq.heappop(pq)[1]
            for v,weight in self.d[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq,[dist[v],v])
        return dist

class directedGraph(Graph):
    pass

class directedUnweightedGraph(directedGraph):
    def add_edge(self,u,v):
        self.d[u].append(v)
        self.size += 1

class directedWeightedGraph(directedGraph):
    def add_edge(self,u,v,weight):
        self.d[u].append([v,weight])
        self.size += 1
    
def main():
    graph:undirectedUnweightedGraph = Graph.exampleUUG()
    graph.printGraph()
    print(graph.bfs(0))
    #print(graph.connected())
    #a = graph.dijkstraAlgo(0)
    #print(a)

if __name__ == "__main__":
    main()

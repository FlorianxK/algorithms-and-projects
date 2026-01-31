from collections import deque
import heapq
from typing import *

class Graph:
    def __init__(self):
        self.d = DefaultDict(list)
        self.size = 0

    def sort(self):
        self.d = dict(sorted(self.d.items()))

    def removeEdge(self,u,v) -> None:
        if v in self.d[u] and u in self.d[v]:
            self.d[u].remove(v)
            self.d[v].remove(u)
        else:
            raise Exception("Nodes are not connected")

    def adjacencyList(self) -> List[int]:
        adj = [[0]*self.size for _ in range(self.size)]
        for u in self.d:
            if isinstance(self.d[u][0], List):
                for v,weight in self.d[u]:
                    adj[u][v] = weight
            else:
                for v in self.d[u]:
                    adj[u][v] = 1
        # for a in adj:
        #     print(a)
        return adj

    def exampleUUG():
        g = undirectedUnweightedGraph()
        g.add_edge(1,2)
        g.add_edge(1,0)
        g.add_edge(2,0)
        g.add_edge(2,3)
        g.add_edge(2,4)
        return g

    def exampleUWG1():
        g = undirectedWeightedGraph()
        g.add_edge(0,1,4)
        g.add_edge(0,2,8)
        g.add_edge(1,4,6)
        g.add_edge(2,3,2)
        g.add_edge(3,4,10)
        return g

    def exampleUWG2():
        g = undirectedWeightedGraph()
        g.add_edge(0,1,4)
        g.add_edge(0,2,2)
        g.add_edge(0,3,6)
        g.add_edge(1,2,5)
        g.add_edge(1,3,2)
        g.add_edge(2,3,6)
        return g

class undirectedGraph(Graph):

    def hasEulercircuit(self) -> bool:
        oddDegree = 0
        for v in self.d.values():
            if len(v) % 2 != 0:
                oddDegree += 1
        if oddDegree == 0 or oddDegree == 2:
            return True
        else:
            return False

    def dfsCount(self,v,visited):
        visited.add(v)
        for ngh in self.d[v]:
            if ngh not in visited:
                self.dfsCount(ngh,visited)

    def isValidNextEdge(self,u,v) -> bool:
        if len(self.d[u]) == 1:
            return True
        
        if v not in self.d[u]:
            return False

        self.d[u].remove(v)
        self.d[v].remove(u)

        visited = set()
        if u in self.d:
            self.dfsCount(u, visited)
        
        self.d[u].append(v)
        self.d[v].append(u)
        
        return len(visited) > 0 or u not in self.d

    def getEuler(self,u):
        edges = []
        if u not in self.d:
            return edges

        for ngh in list(self.d[u]):
            if self.isValidNextEdge(u,ngh):
                edges.append([u,ngh])
                self.removeEdge(u,ngh)
                edges.extend(self.getEuler(ngh))
        return edges

    #find one eulercircuit
    def fleuryAlgorithm(self):
        start = None
        for k,v in self.d.items():
            if len(v) % 2 != 0:
                start = k
                break
        
        if start == None:
            start = next(iter(self.d))
        
        edges = self.getEuler(start)
        return edges

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
        self.size = len(self.d)

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
        self.size = len(self.d)

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

    def greedyTravelingSalesmanProblem(self,src):
        visited = set()
        route = [src]
        visited.add(src)
        total_dist = 0

        while True:
            last = route[-1]
            nearest = None
            min_dist = float("inf")
            for neigh in self.d[last]:
                if neigh[1] < min_dist and neigh[0] not in visited:
                    min_dist = neigh[1]
                    nearest = neigh[0]
            if nearest != None:
                route.append(nearest)
                visited.add(nearest)
                total_dist += min_dist
            else:
                break

        for a,b in self.d[route[-1]]:
            if a == src:
                total_dist += b
                route.append(src)
                return route,total_dist

    def dpTravelingSalesmanProblem(self,cost):
        if self.size <= 1:
            return cost[0][0] if self.size == 1 else 0
        
        FULL = 1 << self.size
        fullMask = FULL-1

        dp = [ [float("inf")]*self.size for _ in range(FULL) ]
        dp[1][0] = 0

        for mask in range(1,FULL):
            for i in range(self.size):
                if not (mask & (1 << i)):
                    continue
                if dp[mask][i] == float("inf"):
                    continue
                for j in range(self.size):
                    if mask & (1 << j):
                        continue
                    nxt = mask | (1 << j)

                    dp[nxt][j] = min( dp[nxt][j], dp[mask][i]+cost[i][j] )

        res = float("inf")
        for i in range(self.size):
            if dp[fullMask][i] != float("inf"):
                res = min(res, dp[fullMask][i]+cost[i][0] )

        return res

    def kruskalAlgo(self):

        def find(parent,i):
            if parent[i] != i:
                parent[i] = find(parent,parent[i])
            return parent[i]
        
        def union(parent,rank,x,y):
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = y
            else:
                parent[y] = x
                rank[x] += 1

        h = []
        for u,l in self.d.items():
            for v,weight in l:
                heapq.heappush(h, (weight,u,v) )
        
        parent = []
        rank = []
        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        mst = DefaultDict(list)
        cost = 0
        while h:
            minEdge = heapq.heappop(h)
            weight,u,v = minEdge
            x = find(parent,u)
            y = find(parent,v)

            if x != y:
                cost += weight
                mst[u].append([v,weight])
                mst[v].append([u,weight])
                union(parent,rank,x,y)
        
        return mst,cost

class directedGraph(Graph):
    pass

class directedUnweightedGraph(directedGraph):
    def add_edge(self,u,v):
        self.d[u].append(v)
        self.size = len(self.d)

class directedWeightedGraph(directedGraph):
    def add_edge(self,u,v,weight):
        self.d[u].append([v,weight])
        self.size = len(self.d)
    
def main():
    graph:undirectedWeightedGraph = Graph.exampleUWG2()
    # graph:undirectedUnweightedGraph = Graph.exampleUUG()
    # graph.printGraph()
    graph.printGraph()
    mst,cost = graph.kruskalAlgo()
    print(mst,cost)
    # a = graph.fleuryAlgorithm()
    # print(a)

    #print(graph.connected())
    #a = graph.dijkstraAlgo(0)
    #print(a)

if __name__ == "__main__":
    main()

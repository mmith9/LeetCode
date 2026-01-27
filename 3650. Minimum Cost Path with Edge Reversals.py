from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List

#beats 100%
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        for a, b, w in edges:
            dests = graph[a]
            if b not in dests or w < dests[b]:
                dests[b] = w
            dests = graph[b]
            if a not in dests or 2*w < dests[a]:
                dests[a] = 2*w
                
        visited = [False]*n
        n -= 1; inf = 10**12; distances = [0] + [inf]*n
        heap = [];heappush(heap,(0,0))

        while heap:
            nodedist, node = heappop(heap)
            if node == n:
                return nodedist
            if visited[node] or distances[node] != nodedist:
                continue
            visited[node] = True

            dests = graph[node]
            for nextnode in dests:
                if not visited[nextnode]:
                    nextdist = dests[nextnode] + nodedist
                    if distances[nextnode] > nextdist:
                        distances[nextnode] = nextdist
                        heappush(heap, (nextdist, nextnode))

        return -1


engine = Solution()

n = 4; edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
print(engine.minCost(n, edges), 5)

n = 4; edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
print(engine.minCost(n, edges), 3)




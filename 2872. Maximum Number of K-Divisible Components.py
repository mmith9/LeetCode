from typing import List

#simple tree indepth traverse, nothing fancy, most good results are similar
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0]
        def traverse(v:int, parent:int) -> int:
            sum_ = values[v]
            for kid in graph[v]:
                if kid != parent:
                    sum_ += traverse(kid, v)

            if sum_ % k:
                return sum_
            res[0]+=1
            return 0
            
        traverse(0, -1)
        return res[0]
    

engine = Solution()

n = 5; edges = [[0,2],[1,2],[1,3],[2,4]]; values = [1,8,1,4,4]; k = 6
print(engine.maxKDivisibleComponents(n, edges, values, k),2 )

n = 7; edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]; values = [3,0,6,1,5,2,1]; k = 3
print(engine.maxKDivisibleComponents(n, edges, values, k),3 )



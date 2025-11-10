from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        cons = defaultdict(set)
        for a,b in connections:
            cons[a].add(b)
            cons[b].add(a)
        
        groups = [0]
        plant2group = [0]*(c+1)

        def walk_graph(groupnum, node):
            plant2group[node] = groupnum
            groups[groupnum].append(node)
            for adjacent in cons[node]:
                if not plant2group[adjacent]:
                    walk_graph(groupnum, adjacent)

        for node in range(1,c+1):
            if plant2group[node]:
                continue
            groupnum = len(groups)
            groups.append([])
            walk_graph(groupnum, node)

#        print(groups)
# part2, process queries
        for group in groups[1:]:
            heapify(group)
            
        states = [True]*(c+1)
        result = []

        for opcode, node in queries:
            if opcode == 2:
                states[node] = False
                continue
            #opcode is 1
            if states[node]:
                result.append(node)
                continue
            #get lowest from group
            heap = groups[plant2group[node]]
            while heap and not states[heap[0]]:
                heappop(heap)
            
            if heap:
                result.append(heap[0])
            else:
                result.append(-1)
        return result
    


engine = Solution()
c = 5; connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
print(engine.processQueries(c, connections, queries))
print([3,2,3])


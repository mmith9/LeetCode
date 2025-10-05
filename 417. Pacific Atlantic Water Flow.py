from typing import List, Set
from heapq import heapify, heappop, heappush

#boundary consumption
#pacific up left, atlantic down right
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        lenx = len(heights[0]); max_x = lenx-1
        leny = len(heights); max_y = leny-1
        heap_a = []; visited_a = set()
        heap_p = []; visited_p = set()

        for x,h in enumerate(heights[0]):
            heap_p.append((h,x,0))
            visited_p.add((x,0))
        for x,h in enumerate(heights[max_y]):
            heap_a.append((h,x,max_y))
            visited_a.add((x,max_y))
        for y in range(leny):
            heap_p.append((heights[y][0],0,y))
            visited_p.add((0,y))
            heap_a.append((heights[y][max_x],max_x,y))
            visited_a.add((max_x,y))

        def walk_up(heap:List, visited:Set) ->None:
            heapify(heap)
            while heap:
                h,x,y = heappop(heap)
                for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                    if 0<=i<=max_x and 0<=j<=max_y and (i,j) not in visited:
                        if heights[j][i] >= h:
                            visited.add((i,j))
                            heappush(heap, (heights[j][i], i,j))
        
        walk_up(heap_p, visited_p)
        walk_up(heap_a, visited_a)
        result = []
        for x,y in visited_a.intersection(visited_p):
            result.append([y,x]) ## coordinates are reveresed in answer
        return result    

engine = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(engine.pacificAtlantic(heights))
print([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])




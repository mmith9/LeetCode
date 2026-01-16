from collections import defaultdict
from itertools import pairwise
from typing import List
from bisect import insort_left

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        edges = defaultdict(list); target = 0
        for left, down, a in squares:
            edges[down].append((1, left, left+a))
            edges[down+a].append((0, left, left+a))
            
        cur_edges = []; got = 0; cache = []
        def update_cur_edges(y):
            for add, a, b in edges[y]:
                if add:
                    insort_left(cur_edges, (a, b))
                else:
                    cur_edges.remove((a, b))

            width = 0; left = 0
            for a, b in cur_edges:
                if a >= left:
                    width += (b - a)
                    left = b
                elif b > left:
                    width += (b - left)
                    left = b
                #else skip
            return width                        

        for y,nexty in pairwise(sorted(edges)):
            width = update_cur_edges(y)
            got += (nexty - y) * width
            cache.append((nexty, width, got))
        
        target = got/2
        for entry in cache:
            if entry[2] >= target:
                return entry[0] - (entry[2] - target) / entry[1]

#######
# solution using range list. Supposed to be faster XD
# test cases are specifically designed to TLE it

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        edges = defaultdict(list); 
        for left, down, a in squares:
            edges[down].append((1, left, left+a))
            edges[down+a].append((0, left, left+a))
            
        cur_edges = []
        # cur_edges = list of (left, right, count)
        def update_cur_edges2(y):
#            print('now', cur_edges)
            dif = 0
            print('updating', len(edges[y]))
            for add, a, b in edges[y]:
#                print('change', add, a, b)
                if add:
                    dif += u2_add(a,b)
                else:
                    dif += u2_rm(a,b)
#                print('result', dif, cur_edges)
            return dif
        
        def u2_add(a,b):
            replace = []; count = dif = 0
            where = bisect_left(cur_edges, (a,0,0))
            if where >0:
                if cur_edges[where -1][1]>a:
                    where -=1

            for i,j,cnt in cur_edges[where:]:
                if a<i:
                    if b<=i:
                        replace.append((a,b,1))
                        dif += b-a
                        a = b
                        break
                    replace.append((a,i,1))
                    dif += i - a
                    a=i
                elif i<a:
                    replace.append((i,a, cnt))
                
                count += 1
                if b <= j:  # (i (a,b) j)
                    replace.append((a,b,cnt+1))
                    if b < j:
                        replace.append((b,j, cnt))
                    a = b
                    break
            
                replace.append((a,j,cnt+1))
                a = j
            
            if a < b:
                replace.append((a,b,1))
                dif += b - a

            cur_edges[where:where+count] = replace
            return dif

        #ranges always exist in this case, so much simpler code
        def u2_rm(a,b):
            replace = []; count = dif = 0
            where = bisect_left(cur_edges, (a,0,0))
            for i, j, cnt in cur_edges[where:]:
                count += 1
                assert a == i
                if cnt >1:
                    replace.append((i,j,cnt-1))
                else:
                    dif -= j - i
                if b == j:
                    break
                a = j
            cur_edges[where:where+count] = replace
            return dif

        def update_cur_edges(y):
            for add, a, b in edges[y]:
                if add:
                    insort_left(cur_edges, (a, b))
                else:
                    cur_edges.remove((a, b))

            width = 0; left = 0
            for a, b in cur_edges:
                if a >= left:
                    width += (b - a)
                    left = b
                elif b > left:
                    width += (b - left)
                    left = b
                #else skip
            return width                        

        width = 0; got = 0; cache = []
        for y,nexty in pairwise(sorted(edges)):
#            width = update_cur_edges(y)
            width += update_cur_edges2(y)
#            print(width)
            got += (nexty - y) * width
            cache.append((nexty, width, got))
        
        target = got/2
        for entry in cache:
            if entry[2] >= target:
                return entry[0] - (entry[2] - target) / entry[1]





engine = Solution()

# squares = [[0,0,1],[2,2,1]]
# print(engine.separateSquares(squares),1.0)

# squares = [[0,0,2],[1,1,1]]
# print(engine.separateSquares(squares),1.0)

squares = [[15,21,2],[19,21,3]]
print(engine.separateSquares(squares),22.3)
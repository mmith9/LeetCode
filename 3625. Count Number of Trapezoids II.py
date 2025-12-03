from collections import defaultdict
import math
from typing import List

#analytical, integer mathematics only, relatively fast
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        #line is Ax+By=C, return normalized abc, where (A,B) are coprimes and B >=0. l2 is length^2 to avoid roots

        # slope = lines [(a,b)] 
        # group = slope [c]
        # group is dict l2 -> count of lines of l2
        edges = defaultdict(lambda:defaultdict(lambda:defaultdict(int)))

        # We are grouping edges by:
        # by slope = (a,b) in canonical form
        # by C which separates edges on different lines
        # by edge length

        while points:
            x1, y1 = points.pop()
            for x2,y2 in points:
                a = y2 - y1
                b = x1 - x2
                l2 = a*a + b*b

                if b < 0:
                    a, b = -a, -b
                elif b == 0:
                    a = abs(a)
                
                gcd = math.gcd(a, b)
                if gcd > 1:
                    a, b = a//gcd, b//gcd

                c = a*x1 + b*y1
                edges[(a,b)][c][l2] += 1

        traps = 0; paras = 0 # trapezoids and parralelograms

        for edgesp in edges.values():  #group by parralel edges
            tot_t = 0; tot_dif = 0; par = defaultdict(list)

            for edgesl in edgesp.values(): # group by distinct lines
                cnt = 0
                for key, value in edgesl.items():
                    cnt += value
                    par[key].append(value)
                cnt = sum(edgesl.values())
                tot_t += cnt
                tot_dif += cnt*(cnt-1)
                              
            # count parralelograms
            for edges in par.values(): #grouped by same length
                if len(edges) <2:
                    continue
                tot_p = 0; tot_dif_p = 0
                for x in edges:
                    tot_p += x
                    tot_dif_p += x*(x-1)
                paras += tot_p*(tot_p-1) - tot_dif_p

            traps += tot_t*(tot_t-1) - tot_dif

#        print(traps, paras)
        # both trapezoids and parralelograms are counted double because omitted //2 in combination formula
        return (traps - paras//2) //2
    


engine = Solution()


# points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
# print(engine.countTrapezoids(points), 2)

# points =  [[0,0],[1,0],[0,1],[2,1]]
# print(engine.countTrapezoids(points), 1)

points = [[10,-66],[-36,30],[86,30],[10,30],[-75,19],[83,19],[86,19],[-39,19]]
print(engine.countTrapezoids(points), 1)

points = [[-36,30],[86,30],[83,19],[-39,19]]
print(engine.countTrapezoids(points), 1)



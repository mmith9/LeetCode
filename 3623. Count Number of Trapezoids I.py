from collections import defaultdict
from itertools import pairwise
from math import comb
from typing import List

#only need pairs where y1==y2
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ygreks = defaultdict(int)
        for _, y in points:
            ygreks[y]+=1
        
        sum = 0; res = 0
        for ixes in ygreks.values():
            if ixes > 1:
                edges = ixes*(ixes-1)//2
                res += edges * sum 
                sum += edges
        
        return res % 1_000_000_007

engine = Solution()

points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
print(engine.countTrapezoids(points),3)


points = [[0,0],[1,0],[0,1],[2,1]]
print(engine.countTrapezoids(points),1)





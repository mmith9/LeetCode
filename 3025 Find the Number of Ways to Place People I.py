from typing import List
# list(a,b) ax<=bx ay>=by, nothing inbetween

#naive optimized
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pairs = 0
        for idx1, (ax,ay)  in enumerate(points):
            for idx2, (bx,by) in enumerate(points):
                if idx1 != idx2 and ax <= bx and ay >= by:
                    for idx3, (cx,cy) in enumerate(points):
                        if idx1 == idx3 or idx2 == idx3:
                            continue
                        if ax <= cx <= bx and ay>=cy>=by:
                            break
                    else:
                        pairs +=1
        return pairs

from typing import List
# list(a,b) ax<=bx ay>=by, nothing inbetween
#geometrical optimized
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0]-x[1]/1000)
        pairs = 0
        for idx1, (_,ay)  in enumerate(points):
            cur_low = -100 #below max
            for _, by in points[idx1+1:]:
                if ay >= by > cur_low:
                    pairs+=1
                    if by == ay:
                        break
                    cur_low = by

        return pairs


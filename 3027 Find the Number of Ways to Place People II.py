from typing import List
# list(a,b) ax<=bx ay>=by, nothing inbetween
#geometrical optimized
inf = 10**10
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],-x[1]))
        pairs = 0
        for idx1, (_,ay)  in enumerate(points):
            cur_low = -inf #below max
            for _, by in points[idx1+1:]:
                if ay >= by > cur_low:
                    pairs+=1
                    if by == ay:
                        break
                    cur_low = by

        return pairs


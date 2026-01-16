from itertools import pairwise
from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        if not hBars or not vBars:
            return 1
        if len(hBars) == 1 or len(vBars) == 1:
            return 4
            
        hBars.sort(); vBars.sort()

        hc = hmax = 2
        for a,b in pairwise(hBars):
            hc = hc + 1 if a+1 == b else 2
            if hc > hmax: hmax = hc

        vc = vmax = 2
        for a,b in pairwise(vBars):
            vc = vc + 1 if a+1 == b else 2
            if vc > vmax: vmax = vc

        return (min(hmax,vmax))**2
            



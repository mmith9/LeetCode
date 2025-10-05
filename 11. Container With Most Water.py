
#beats 99%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0; end=len(height) -1
        max_h = max(height)
        vol = 0
        while start<end:
            left = height[start]
            right = height[end]
            cur_vol = min(left,right)*(end-start)
            if cur_vol > vol:
                vol = cur_vol

            if (end-start)*max_h <= vol: #won't find anything better
                return vol
            
            if left < right:
                start += 1
                while height[start] <= left and start<end:
                    start+=1
            else:
                end -= 1
                while height[end] <= right and start<end:
                    end -= 1
        return vol

from itertools import combinations
from typing import List
#naive, TLE
class Solution:
    def maxArea(self, height: List[int]) -> int:
        indexes = [x for x in range(len(height))]
        vol = 0
        for a,b in combinations(indexes,2):
            cur_vol = min(height[a],height[b])*abs(a-b)
            if cur_vol > vol:
                vol = cur_vol
        return vol
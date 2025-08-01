from typing import List
class Solution_naive:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rct = 0
        max_x = len(heights)
        for x in range(max_x):
            for y in range(x, max_x):
                cur_rct = (y-x+1) * min(heights[x:y+1])
                max_rct = max(cur_rct, max_rct)
        return max_rct
    
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_x = len(heights)
        last_h = 0
        max_rct = max_x * min(heights)

        if heights[0] < heights[-1]:
            heights.reverse()

        for x in range(max_x):
            if heights[x] <= last_h:
                last_h = heights[x]
                continue
            x_left = max_x - x
            cur_min_h = heights[x]            
            if max_rct >= cur_min_h * x_left:
                continue
            max_rct = max(max_rct, cur_min_h)
            for y in range(x+1, max_x):
                if heights[y] >= cur_min_h:
                    continue
                max_rct = max(max_rct, (y-x) * cur_min_h)                
                cur_min_h = heights[y]
                max_rct = max(max_rct, (y-x+1) * cur_min_h)
                if max_rct >= cur_min_h * x_left:
                    break
            max_rct = max(max_rct, cur_min_h * x_left)
            last_h = heights[x]
        
        return max_rct
    
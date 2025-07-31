from typing import List


class Solution_1:
    def trap(self, height: List[int]) -> int:
        max_h = max(height)
        min_h = min(height)
        max_x = len(height)

        capacity = 0
        for h in range(min_h,max_h+1):
            walled = False
            last_wall = -1
            for x in range(max_x):
                is_wall = height[x] >= h
                if is_wall:
                    if last_wall>=0:
                        capacity += x - last_wall -1
                    last_wall = x
        return capacity
    
class Solution_2:
    def trap(self, height: List[int]) -> int:
        max_h = max(height)
        min_h = min(height)
        max_x = len(height)

        x = 0
        capacity = 0
        try_lower = 0
        while x < max_x:
            curr_cap = 0
            left_h = height[x]
            if try_lower>0:
                left_h = try_lower
                try_lower = 0

            max_h_found = 0
            if left_h == 0:
                x+=1
                continue
            for y in range(x+1, max_x):
                curr_h = height[y]
                is_wall = curr_h >= left_h
                if is_wall:
                    capacity += curr_cap
                    x = y
                    break
                curr_cap += left_h - height[y]
                max_h_found = max(max_h_found, curr_h)
            else:
                try_lower = max_h_found
                if not try_lower:
                    return capacity
                
        return capacity

class Solution:
    def trap(self, height: List[int]) -> int:
        max_x = len(height)

        x = 0
        capacity = 0
        while x < max_x-1:
            next_max_h = max(height[x+1:])
            if not next_max_h:
                return capacity
            left_h = min(next_max_h, height[x])
            
            for y in range(x+1, max_x):
                if height[y] >= left_h:
                    x = y
                    break
                capacity += left_h - height[y]
        return capacity      

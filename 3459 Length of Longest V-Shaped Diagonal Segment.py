from functools import lru_cache
from typing import List
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        max_x = len(grid[0])
        max_y = len(grid)

        @lru_cache(maxsize=None)
        def go_dir(x, y, dir_x, dir_y, can_turn, need) -> int:
            cur_x = x+dir_x
            cur_y = y+dir_y
           
            if 0 <= cur_x < max_x and 0 <= cur_y < max_y and grid[cur_y][cur_x] == need:
                max_v = go_dir(cur_x, cur_y, dir_x, dir_y, can_turn, (need+2)%4)
                if can_turn:
                    if dir_x * dir_y >0:
                        dir_x = - dir_x
                    else:
                        dir_y = - dir_y
                    max_v = max(max_v, go_dir(cur_x, cur_y, dir_x, dir_y, False, (need+2)%4))
                return max_v +1
            else:
                return 0

        def find_v_at(x, y) -> int:
            lens = []
            lens.append(go_dir(x, y, 1, 1, True, 2))
            lens.append(go_dir(x, y, -1, 1, True, 2))
            lens.append(go_dir(x, y, -1, -1, True, 2))
            lens.append(go_dir(x, y, 1, -1, True, 2))
            return (max(lens) +1)

        max_v = 0
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 1:
                    max_v = max(max_v, find_v_at(x,y))
        return max_v
    

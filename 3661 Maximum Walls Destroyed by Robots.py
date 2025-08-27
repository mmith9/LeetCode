from functools import lru_cache
from typing import List

import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        max_rob = len(robots) -1
        
        shooters = []
        for pos, dist in zip(robots, distance):
            shooters.append((pos, dist))
        del robots
        del distance
        shooters.sort(key=lambda x: x[0])
        walls.sort()

        @lru_cache(maxsize = None)
        def cnt_walls(start, end) -> int:            
            return bisect.bisect_right(walls, end) - bisect.bisect_left(walls, start)

        @lru_cache(maxsize = None)
        def cnt(num, dir) -> int:
            if num > max_rob:
                return 0
            
            pos, dist = shooters[num]
            
            if dir == 0:
                next = max(cnt(num+1, 0), cnt(num+1,1))
                max_left = pos - dist
                if num>0:
                    max_left = max(max_left, shooters[num-1][0]+1)
                walls_to_left = cnt_walls(max_left, pos)
                return next + walls_to_left
            
            if num == max_rob:
                return cnt_walls(pos, pos+dist)

            next_pos, next_dist = shooters[num +1]
            if pos + dist >= next_pos - next_dist:
                return max(
                    cnt_walls(pos, min(pos+dist, next_pos-1)) + cnt(num+1,1),
                    cnt_walls(pos, next_pos) + max(cnt(num+2, 0), cnt(num+2, 1))
                )
            return cnt_walls(pos, pos+dist) + max(cnt(num+1, 0), cnt(num+1, 1))
        return max(cnt(0, 0), cnt(0, 1))
    
from functools import lru_cache
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        max_robs = len(robots) -1
        len_walls = len(walls)
        skip_walls = 0
        skip_walls_right = len_walls

        shoters = []
        for pos, dist in zip(robots, distance):
            shoters.append((pos, dist))
        shoters.append((10**11,0)) #bogus
        del robots
        del distance
        shoters.sort(key=lambda x: x[0])
        walls.sort()

        @lru_cache(maxsize = None)
        def cnt_walls(start, end) -> int:     
            nonlocal skip_walls
            nonlocal skip_walls_right
            pos_s = bisect_left(walls, start, lo=skip_walls, hi=skip_walls_right)
            return bisect_right(walls, end, lo=pos_s, hi=skip_walls_right) - pos_s            

        @lru_cache(maxsize = None)
        def cnt(num, dir, max_rob = max_robs) -> int:
            if num > max_rob:
                return 0
            
            pos, dist = shoters[num]
            
            if dir == 0:
                next = max(cnt(num+1, 0, max_rob), cnt(num+1, 1, max_rob))
                max_left = pos - dist
                if num>0:
                    max_left = max(max_left, shoters[num-1][0]+1)
                walls_to_left = cnt_walls(max_left, pos)
                return next + walls_to_left
            
            if num == max_rob:
                return cnt_walls(pos, pos+dist)

            next_pos, next_dist = shoters[num +1]
            if pos + dist >= next_pos - next_dist:
                return max(
                    cnt_walls(pos, min(pos+dist, next_pos-1)) + cnt(num+1,1, max_rob),
                    cnt_walls(pos, next_pos) + max(cnt(num+2, 0, max_rob), cnt(num+2, 1, max_rob))
                )
            return cnt_walls(pos, pos+dist) + max(cnt(num+1, 0, max_rob), cnt(num+1, 1, max_rob))

        max_walls = 0
        last_droid = -1

        # print(shoters)
        # print(walls)
        for num, shoter in enumerate(shoters[:-1]):
            pos, dist = shoter
            nex_pos, nex_dist = shoters[num+1]

            if pos+dist < nex_pos - nex_dist:
                # print('noclip', num, max_walls)
                if last_droid >= 0:
                    skip_walls_right = bisect_right(walls, pos+dist, lo=skip_walls)
                    max_walls += max(cnt(last_droid, 0, num), cnt(last_droid, 1, num))
                    last_droid = -1
                else:
                    walls_right = bisect_right(walls, pos + dist, lo = skip_walls)
                    walls_left = bisect_left(walls, pos - dist, lo=skip_walls, hi=walls_right)
                    walls_onr = bisect_left(walls, pos, lo=walls_left, hi=walls_right)
                    walls_onl = walls_onr
                    if walls_onr<len_walls and walls[walls_onr] == pos:
                        walls_onl+=1      
                    max_walls += max(walls_onl - walls_left, walls_right - walls_onr)
                    skip_walls = walls_right

            else:
                # print('clip', num, max_walls)                
                if last_droid < 0:
                    last_droid = num
                else:
                    pass

        if last_droid>=0:
            skip_walls_right = len_walls
            max_walls += max(cnt(last_droid, 0, max_robs), cnt(last_droid, 1, max_robs))

        return max_walls
            
    
from bisect import bisect_right
from typing import List
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        lenx = len(rains); maxx = lenx-1
        filled = {}
        dry_days = []
        flushes = [1 for _ in range(lenx)]

        for day in range(lenx):
            lake = rains[day]
            if not lake:
                dry_days.append(day)
                continue
            
            elif lake in filled:
                fill_day = filled[lake]
                idx = bisect_right(dry_days, fill_day)
                if idx == len(dry_days):
                    return []
                flush_day = dry_days.pop(idx)
                flushes[flush_day] = lake

            filled[lake] = day
            flushes[day] = -1

        return flushes
    
engine = Solution()


# rains = [1,2,0,0,2,1]
# print(engine.avoidFlood(rains))
# print([-1,-1,2,1,-1,-1])

# rains = [69,0,0,0,69]
# print(engine.avoidFlood(rains))
# print([-1,69,1,1,-1])

rains = [1,0,2,0,2,1]
print(engine.avoidFlood(rains))
from bisect import bisect_left
from sortedcontainers import SortedSet
inf = 10**6
class RangeModule:
    
    def __init__(self):
        self.ranges = SortedSet()

    def addRange(self, left: int, right: int) -> None:
        idx = bisect_left(self.ranges, (left, -inf))
        if idx > 0: #sumthing to left
            if self.ranges[idx-1][1] >= left: # left clips range
                r_l, r_r = self.ranges.pop(idx-1)
                if r_r >= right: # left actually encompasses range
                    self.ranges.add((r_l, r_r))
                    return
                left = r_l # merge left one to current
                idx -= 1
        #consume ranges to right if clip
        while idx < len(self.ranges) and self.ranges[idx][0] <= right: # right clips 
            r_l, r_r = self.ranges.pop(idx)
            if r_r >= right: 
                right = r_r
                break
            # else, range encompasses right range, proceed to next
        self.ranges.add((left, right))

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False

        idx = bisect_left(self.ranges, (left, -inf))
        if idx >= len(self.ranges):
            idx -=1            
        
        if 0 < idx and self.ranges[idx-1][1] > left: 
            idx -= 1            
        r_l, r_r = self.ranges[idx]
        return r_l <= left and r_r >= right

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges:
            return
        idx = bisect_left(self.ranges, (left, -inf))
        if idx > 0: #sumthing to left
            if self.ranges[idx-1][1] > left: # left clips range
                r_l, r_r = self.ranges.pop(idx-1)
                if r_l < left:
                    self.ranges.add((r_l, left))
                else:
                    idx -= 1
                if r_r >= right: # left actually encompasses range
                    if r_r > right:
                        self.ranges.add((right, r_r))
                    return

        #consume ranges to right if clip
        while idx < len(self.ranges) and self.ranges[idx][0] <= right: # right clips 
            r_l, r_r = self.ranges.pop(idx)
            if r_r > right: 
                self.ranges.add((right, r_r))
                break

            # else, range encompasses right range, proceed to next

params =[[],[6,8],[7,8],[8,9],[8,9],[1,3],[1,8],[2,4],[2,9],[4,6]]
cmds = ["RangeModule","addRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange"]
engine = RangeModule()

for param, cmd in zip(params,cmds):
    print(cmd, param)
    if cmd == 'addRange':
        engine.addRange(param[0], param[1])
        print('add', engine.ranges)

    if cmd == 'removeRange':
        engine.removeRange(param[0], param[1])        
        print('rm', engine.ranges)

    if cmd == 'queryRange':
        result = engine.queryRange(param[0], param[1])        
        print(result)


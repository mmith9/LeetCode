from collections import deque
import itertools
from typing import List
# naive - check collisions vs all lines
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        x=0;y=0;inf = 10**6
        dir_ = 0 #0 north, 1 west, 2 south, 3 east
        cycler = itertools.cycle([(0, 1), (-1, 0), (0, -1), (1, 0)])
        lines_h = deque([(inf,0,0), (inf,0,0), (0,0,0)]); lines_v = deque([(0,0,0), (0,0,0), (0,0,0)])

        for dist in distance:
            dif_x, dif_y = next(cycler)
#            print(x, y, 'to', cur_x, cur_y)
            if dif_x == 0: # v motion
                cur_y = y + dist * dif_y

#                print('V motion')
                for i in range(2):
                    a, b1, b2 = lines_h[i]
#                    print('h line', a, b1, b2)
                    if b1 <= x <= b2 and (y <= a <= cur_y or cur_y <= a <= y) :
#                        print('collision')
                        return True
                if y < cur_y:
                    lines_v.append((x, y, cur_y))
                else:
                    lines_v.append((x, cur_y, y))
                lines_v.popleft()
                y = cur_y
            else:            # h motion
                cur_x = x + dist * dif_x
#                print('h motion')
                for i in range(2):
                    b,a1,a2 = lines_v[i]
#                    print('v line', b, a1, a2)
                    if a1 <= y <= a2 and (x <= b <= cur_x or cur_x <= b <= x):
#                        print('collision')
                        return True
                if x < cur_x:
                    lines_h.append((y, x, cur_x))
                else:
                    lines_h.append((y, cur_x, x))
                lines_h.popleft()         
                x = cur_x; 
        return False



engine = Solution()
distance = [2,1,1,2]
print(engine.isSelfCrossing(distance), True)
distance = [1,2,3,4]
print(engine.isSelfCrossing(distance), False)
distance = [1,1,1,2,1]
print(engine.isSelfCrossing(distance), True)
distance = [1,1,2,1,1]
print(engine.isSelfCrossing(distance), True)

distance = [2,1,1,2]
print(engine.isSelfCrossing(distance), True)

distance = [1,1,2,2,1,1]
print(engine.isSelfCrossing(distance), True)



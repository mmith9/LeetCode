from collections import deque
from typing import List

#reasonable fast 180ms, accelerated by removing from end of the list instead of start

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
       
        res = {}
        queue = []
        for x in range(len(positions)):
            queue.append([positions[x], healths[x], directions[x]])
        queue.sort()

        while queue and queue[-1][2] == 'R':
            droid = queue.pop()
            res[droid[0]] = droid[1]

        tail = []
        while queue:
            if tail:
                droid = tail.pop()
            else:
                droid = queue.pop()
                if droid[2] == 'R':
                    res[droid[0]] = droid[1]
                    continue            

            while queue:
                if queue[-1][2] == 'L':
                    tail.append(droid)
                    droid = queue.pop()

                else:
                    #queued boom
                    if queue[-1][1] < droid[1]:
                        droid[1] -= 1
                        queue.pop()
                        continue
                    
                    #current boom
                    if queue[-1][1] > droid[1]:
                        queue[-1][1]-=1
                        droid = None
                        break

                    #both kaboom
                    queue.pop()
                    droid = None
                    break

        if droid:
            res[droid[0]] = droid[1]

        for droid in tail:
            res[droid[0]] = droid[1]

        res_ord = []
        for pos in positions:
            if pos in res:
                res_ord.append(res[pos])
        return res_ord




#slow 2k ms
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        res = {}

        queue = []
        for x in range(len(positions)):
            queue.append([positions[x], healths[x], directions[x]])
        queue.sort()
        queue = deque(queue)

        while queue:
            while queue and queue[-1][2] == 'R':
                droid = queue.pop()
                res[droid[0]] = droid[1]

            while queue and queue[0][2] == 'L':
                droid = queue.popleft()
                res[droid[0]] = droid[1]
            
            idx = 0
            while idx < len(queue) -1:

                if queue[idx][2] == 'L' or queue[idx+1][2] == 'R':
                    idx += 1
                    continue

                if queue[idx][1] > queue[idx+1][1]:
                    queue[idx][1] -= 1
                    queue.pop(idx+1)
                elif queue[idx][1] < queue[idx+1][1]:
                    queue[idx+1][1] -= 1
                    queue.pop(idx)
                    if idx>0:
                        idx-=1
                else:
                    queue.pop(idx)
                    queue.pop(idx)
                    if idx>0:
                        idx-=1

        res_ord = []
        for pos in positions:
            if pos in res:
                res_ord.append(res[pos])
        return res_ord



engine=Solution()

positions = [5,4,3,2,1]; healths = [2,17,9,15,10]; directions = "RRRRR"
print(engine.survivedRobotsHealths(positions, healths, directions))
print([2,17,9,15,10])


positions = [3,5,2,6]; healths = [10,10,15,12]; directions = "RLRL"
print(engine.survivedRobotsHealths(positions, healths, directions))
print([14])



positions = [1,2,5,6]; healths = [10,10,11,11]; directions = "RLRL"
print(engine.survivedRobotsHealths(positions, healths, directions))
print([])
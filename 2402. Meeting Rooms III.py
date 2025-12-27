from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        uses = [0]*n
        free = list(range(n))
        heapify(free)
        used = [] # tuple(freetime, roomno)
        heapify(used)
        meetings.sort(key = lambda x:x[0])
    
        for start, end in meetings:
            while used and used[0][0] <= start:
                heappush(free, heappop(used)[1])
            if free:
                room = heappop(free)
                heappush(used,(end, room))
            else:
                newstart, room = heappop(used)
                heappush(used,(newstart-start+end, room))
            uses[room] +=1
        
        return uses.index(max(uses))
    


engine = Solution()


n = 2; meetings = [[0,10],[1,5],[2,7],[3,4]]
print(engine.mostBooked(n, meetings), 0)


n = 3; meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
print(engine.mostBooked(n, meetings), 1)
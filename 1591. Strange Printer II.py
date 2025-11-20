from collections import defaultdict
from typing import Dict, List

#proper version with blocking colors management and color scan fast resume.
# and it's somehow slower than plain bruteforce :/ because sorting by size is an actual wrecking ball here
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #color rectangle: list[up,right,down,left]
        colors:Dict[int, List] = {}
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                if color not in colors:
                    colors[color] = [r,c,r,c]
                else:
                    _,right,down,left = colors[color]
                    if right < c:
                        colors[color][1] = c
                    if down<r:
                        colors[color][2] = r
                    if left>c:
                        colors[color][3] = c
                    #up no need to check as it's downscan

        queue = list(colors.keys())
        queue.sort(key=lambda x:(colors[x][2]-colors[x][0]+1)*(colors[x][1]-colors[x][3]+1))
        printed = set([0])
        blocker = defaultdict(int); resumerow = defaultdict(int); blockers = set()
        
        def is_printable(color:int):
            up,right,down,left = colors[color]
            rownum = resumerow[color]
            for row in targetGrid[up+rownum:down+1]:
                for c in row[left:right+1]:
                    if c!=color and c not in printed:
                        resumerow[color] = rownum
                        blocker[color] = c
                        blockers.add(c)
                        return False
                rownum +=1
            printed.add(color)
            blocker[color] = 0
            return True

        while queue:
            for color in queue.copy():
                if blocker[color] in printed and is_printable(color):
                    queue.remove(color)
                    if color in blockers:
                        blockers.discard(color)
                        break
            else: #nothing printable found or exhaused the list
                return not bool(queue)

        return True


from typing import Dict, Iterator, List
#fun version using generators as semaphors for colors
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #area list[up,right,down,left]
        colors:Dict[int, List] = {}
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                if color not in colors:
                    colors[color] = [r,c,r,c]
                else:
                    cc = colors[color]
                    _,right,down,left = cc
                    if right < c:
                        cc[1] = c
                    if down<r:
                        cc[2] = r
                    if left>c:
                        cc[3] = c
                    #up no need to check as it's downscan

        printed = set()

        def is_blocked(color:int) -> Iterator[bool]:
            up,right,down,left = colors[color]
            for row in targetGrid[up:down+1]:
                for c in row[left:right+1]:
                    while c not in printed and c!=color:
                        yield False
            printed.add(color)
            yield True

        queue = list(colors.keys())
        queue.sort(key=lambda x:(colors[x][2]-colors[x][0]+1)*(colors[x][1]-colors[x][3]+1))
        queue = [is_blocked(color) for color in queue]

        while queue:
            for semaphor in queue:
                if next(semaphor):
                    break
            else:
                return False
            queue.remove(semaphor)
        return True

from typing import Dict, List
#first dirty attempt and allready beats 97%
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #area list[up,right,down,left]
        colors:Dict[int, List] = {}
        for r, row in enumerate(targetGrid):
            for c, color in enumerate(row):
                if color not in colors:
                    colors[color] = [r,c,r,c]
                else:
                    cc = colors[color]
                    _,right,down,left = cc
                    if right < c:
                        cc[1] = c
                    if down<r:
                        cc[2] = r
                    if left>c:
                        cc[3] = c
                    #up no need to check as it's downscan

        queue = list(colors.keys())
        queue.sort(key=lambda x:(colors[x][2]-colors[x][0]+1)*(colors[x][1]-colors[x][3]+1))
        printed = set()

        def is_printable(color:int):
            up,right,down,left = colors[color]
            for row in targetGrid[up:down+1]:
                for c in row[left:right+1]:
                    if c not in printed and c!=color:
                        return False
            return True

        while queue:
            for color in queue:
                if is_printable(color):
                    printed.add(color)
                    break
            else: #nothing printable found
                return False
            queue.remove(color)

        return True

engine = Solution()

targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
print(engine.isPrintable(targetGrid), True)

targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
print(engine.isPrintable(targetGrid), True)

targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
print(engine.isPrintable(targetGrid), False)
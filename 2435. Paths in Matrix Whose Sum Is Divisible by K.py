from collections import defaultdict
from math import comb
from typing import List
from collections import deque


#deque rotations - fastest
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if k == 1:
            m = len(grid); n = len(grid[0])
            return comb(m + n - 2, n - 1) % 1000000007        

        zeroline = deque([0]*k); sum = 0
        upline = [zeroline.copy() for _ in range(len(grid[0])-1)]; upline.append(zeroline)
        for cell, num in zip(upline, grid[0]):
            sum = (sum + num) % k
            cell[sum] = 1

        for line in grid[1:]:
            prevcell = None
            newline = []
            for upcell, num in zip(upline, line):
                if prevcell:
                    newcell = deque()
                    for a,b in zip(upcell, prevcell):
                        newcell.append(a+b)
                    upcell = newcell
                upcell.rotate(num)
                newline.append(upcell)
                prevcell = upcell
            upline = newline

        return upline[-1][0] % 1000000007 
    


#array based - faster
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if k == 1:
            m = len(grid); n = len(grid[0])
            return comb(m + n - 2, n - 1) % 1000000007        
        zeroline = [0]*(k+1)
        upline = []; sum = 0
        for num in grid[0]:
            sum = (sum + num) % k
            fresh_cell = zeroline.copy()
            fresh_cell[sum] = 1
            upline.append(fresh_cell)

        for line in grid[1:]:
            prevcell = None
            for upcell, num in zip(upline, line):
                upcycle = upcell[k]
                upcell[k] = (upcycle + num) %k

                if prevcell:
                    prevcycle = prevcell[k]
                    offset = prevcycle - upcycle
                    for x in range(k):
                        upcell[(x+offset)%k] += prevcell[x]
                prevcell = upcell

        lastcell = upline[-1];cycle = lastcell[k]
        return lastcell[(k-cycle)%k] % 1000000007 




#dict based - better for mem
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if k == 1:
            m = len(grid); n = len(grid[0])
            return comb(m + n - 2, n - 1) % 1000000007        
        
        upline = []; sum = 0
        for num in grid[0]:
            sum = (sum + num) % k
            fresh_dict = defaultdict(int); fresh_dict[sum] = 1
            upline.append([0,fresh_dict])

        for line in grid[1:]:
            prevcell = None
            for upcell, num in zip(upline, line):
                upcycle = upcell[0]
                upcell[0] = (upcycle + num) %k

                if prevcell:
                    updict = upcell[1]
                    prevcycle = prevcell[0]
                    prevdict = prevcell[1]
                    offset = prevcycle - upcycle
                    for key,value in prevdict.items():
                        updict[(key+offset)%k] += value
        
                prevcell = upcell

        lastcell = upline[-1];cycle = lastcell[0];lastdict = lastcell[1]
        return lastdict[(k-cycle)%k] % 1000000007


engine = Solution()


grid = [[5,2,4],[3,0,5],[0,7,2]]; k = 3
print(engine.numberOfPaths(grid, k), 2)

grid = [[0,0]]; k = 5
print(engine.numberOfPaths(grid, k), 1)

grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]; k = 1
print(engine.numberOfPaths(grid, k), 10)


grid = [[1],[5],[3],[7],[3],[2],[3],[5]]; k=29
print(engine.numberOfPaths(grid, k), 1)

grid = [[2,2,4],[0,0,2],[0,1,2]]; k = 3
print(engine.numberOfPaths(grid, k), 2)


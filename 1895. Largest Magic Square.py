from typing import List

# bit optimized, 58%

# naive
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res = 1; leny = len(grid); lenx = len(grid[0])
#        print(lenx)
#        print(leny)
#        for row in grid:
#            print(row)

        def is_magic(x:int, y:int, k:int, expected:int) -> bool:
#            print('checking', x, y, k)
            #expected = sum(grid[y][x:x+k])
            for row in grid[y+2:y+k]:
                if expected != sum(row[x:x+k]):
#                    print('not rows')
                    return False

            d = sum(grid[y+i][x+i] for i in range(k))
            if d != expected:
#                print('not diag1')
                return False
            d = sum(grid[y+i][x+k-i-1] for i in range(k))
            if d != expected:
#                print('not diag2')
                return False

            sums = grid[y][x:x+k].copy()
            for row in grid[y+1:y+k]:
                for idx, num in enumerate(row[x:x+k]):
                    sums[idx] += num

            for x in sums:
                if x!=expected:
                    return False

#             for j in range(k):
#                 if expected != sum(grid[y+i][x+j] for i in range(k)):
# #                    print('not cols')
#                     return False
                    
            return True

        sums2 = list(accumulate(grid[0]))
        for y in range(leny):
            if y + res >= leny:
                break
            sums1 = sums2
            sums2 = list(accumulate(grid[y+1]))
            s1 = s2 = 0
            for x in range(lenx-res):
                if x + res >= lenx:
                    break
#                print(s1, sums1)
#                print(s2, sums2)
#                print()
#                print(sums1, sums2)
                for k in range(min(lenx-x, leny-y), res, -1):
#                    print(k)
                    if sums1[x+k-1] - s1 == sums2[x+k-1] - s2:
                        if is_magic(x,y,k, sums2[x+k-1] - s2):
                            if k>res:
                                res = k
                                break
                s1 += grid[y][x]
                s2 += grid[y+1][x]
        
        return res
    




# naive, beats 54%
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res = 1; leny = len(grid); lenx = len(grid[0])

        def is_magic(x:int, y:int, k:int) -> bool:
            expected = sum(grid[y][x:x+k])
            for row in grid[y+1:y+k]:
                if expected != sum(row[x:x+k]):
                    return False

            d = sum(grid[y+i][x+i] for i in range(k))
            if d != expected:
                return False
            d = sum(grid[y+i][x+k-i-1] for i in range(k))
            if d != expected:
                return False

            for j in range(k):
                if expected != sum(grid[y+i][x+j] for i in range(k)):
                    return False
            return True

        for y in range(leny):
            if y + res > leny:
                break
            for x in range(lenx-res):
                if x + res > lenx:
                    break
                for k in range(min(lenx-x, leny-y), res, -1):
                    if is_magic(x,y,k):
                        if k>res:
                            res = k
                            break
        
        return res
    

engine = Solution()


grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
print(engine.largestMagicSquare(grid), 3)

grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
print(engine.largestMagicSquare(grid), 2)

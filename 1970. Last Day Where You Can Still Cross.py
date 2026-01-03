from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for _ in range(row)]
        row -= 1; col -= 1
        for r, c in cells:
            grid[r-1][c-1] = 1


        def find_land(r:int, c:int) -> int:
            if r<row and grid[r+1][c] >1:
                return grid[r+1][c]
            if r>0 and grid[r-1][c] >1:
                return grid[r-1][c]
            if c<col and grid[r][c+1] >1:
                return grid[r][c+1]
            if c>0 and grid[r][c-1] >1:
                return grid[r][c-1]
            return 0

        def walk(r:int, c:int, where:int) -> bool:
            if not where:
                where = find_land(r, c)
                if not where: #no connected land adjacent
                    grid[r][c] = 0
                    return False
            
            found = 5 - where
            to_walk = set()

            while True:
                grid[r][c] = where
                if (where == 2 and r == row) or (where == 3 and r == 0):
                    return True
                
                if r<row:
                    state = grid[r+1][c]
                    if not state:
                        to_walk.add((r+1,c))
                    elif state == found:
                        return True
                
                if r>0:
                    state = grid[r-1][c]
                    if state == 0:
                        to_walk.add((r-1,c))
                    elif state == found:
                        return True

                if c<col:
                    state = grid[r][c+1]
                    if not state:
                        to_walk.add((r,c+1))
                    elif state == found:
                        return True
                if c>0:
                    state = grid[r][c-1]
                    if not state:
                        to_walk.add((r,c-1))
                    elif state == found:
                        return True

                if to_walk:
                    r,c = to_walk.pop()
                else:
                    return False

        #not needed, supposedly starts full covered anyway
        # for c, state in enumerate(grid[0]):
        #     if state == 0:
        #         if walk(0, c, 2):
        #             return len(cells)
        
        # for c, state in enumerate(grid[row]):
        #     if state == 0:
        #         walk(row, c, 3)

        while cells:
            r,c = cells.pop()
            r -= 1; c -= 1
            
            if r == 0:
                where = 2
            elif r == row:
                where = 3
            else:
                where = 0

            if walk(r, c, where):
                return len(cells)
        
        return 0

engine = Solution()
row = 2; col = 2; cells = [[1,1],[2,1],[1,2],[2,2]]
print(engine.latestDayToCross(row, col, cells), 2)

row = 2; col = 2; cells = [[1,1],[1,2],[2,1],[2,2]]
print(engine.latestDayToCross(row, col, cells), 1)



row = 3; col = 3; cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
print(engine.latestDayToCross(row, col, cells), 3)


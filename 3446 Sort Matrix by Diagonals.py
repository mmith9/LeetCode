from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        max_n = len(grid)
        diags = [[] for _ in range(max_n*2)]

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                diags[max_n +x -y].append(val)

        new_grid = [[] for _ in range(max_n)]

        for num, row in enumerate(diags):
            if num>max_n:
                row.sort(reverse=True)
            else:
                row.sort()

        for y in range(max_n):
            for x in range(max_n):
                new_grid[y].append(diags[max_n +x -y].pop())

        return new_grid



        
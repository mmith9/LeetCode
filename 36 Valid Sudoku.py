from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        groups = [[] for _ in range(3)]
        for y, line in enumerate(board):
            row = rows[y]
            for x, val in enumerate(line):
                if val.isnumeric():
                    row.append(val)
                    cols[x].append(val)
                    groups[x//3].append(val)
            if len(row) != len(set(row)):
                return False
            if y % 3 == 2:
                for group in groups:
                    if len(group) != len(set(group)):
                        print('group fail')
                        return False
                groups = [[] for _ in range(3)]
        for col in cols:
            if len(col) != len(set(col)):
                return False
        return True
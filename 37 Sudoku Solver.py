from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        board 9x9
        number 1-9 in each row, each column, each 3x3 sub box
        """
        groups = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        blanks = []
        nums_1_to_9 = set(['4','5','6','7','8','9','1','2','3',])

        for x in range(9):
            for y in range(9):
                item = board[y][x]
                if item == '.':
                    blanks.append((x,y))
                else:
                    groups[y//3*3 + x//3].add(item)
                    columns[x].add(item)
        max_pos = len(blanks)

        def try_solving(pos) -> bool:
            if pos >= max_pos:
                return True
            x,y = blanks[pos]
            group = y//3*3 + x//3
            for num in nums_1_to_9:
                if num not in columns[x] and num not in board[y] and num not in groups[group]:
                    board[y][x] = num
                    columns[x].add(num)
                    groups[group].add(num)
                    if try_solving(pos+1):
                        return True
                    columns[x].remove(num)
                    groups[group].remove(num)
            board[y][x] = '.'        
            return False
        
        try_solving(0)

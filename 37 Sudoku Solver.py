from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        board 9x9
        number 1-9 in each row, each column, each 3x3 sub box
        """

        try_solving(board)

def try_solving(board) -> bool:
    for y, row in enumerate(board):
        if '.' in row:
            x = row.index('.')
            possible_nums = find_possible_nums(board, y, x)
            for num in possible_nums:
                board[y][x] = num
                if try_solving(board):
                    return True
            else:
                board[y][x] = '.'
                return False        
    return True

nums_1_to_9 = set(['1','2','3','4','5','6','7','8','9'])
def find_possible_nums(board, row, col) -> Set[str]:
    nums = nums_1_to_9.difference(board[row])
    for y in range(9):
        nums.difference_update(board[y][col])
    sub_row = int(row/3) *3
    sub_col = int(col/3) *3
    for y in range(sub_row, sub_row+3):
        nums.difference_update(board[y][sub_col:sub_col+3])
    
    return nums
    
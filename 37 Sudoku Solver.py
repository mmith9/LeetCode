from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        board 9x9
        number 1-9 in each row, each column, each 3x3 sub box
        """
        self.board = board
        self.spaces = []
        self.cols = [[] for _ in range(9)]
        self.groups = [[] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[y][x]
                if num == '.':
                    self.spaces.append((x,y))
                else:
                    self.groups[y//3*3 + x//3].append(num)
                    self.cols[x].append(num)

        self.try_solving(0)

    def try_solving(self, pos) -> bool:
        if pos >= len(self.spaces):
            return True
        x,y = self.spaces[pos]
        group = y//3 *3 + x//3
        for num in nums_1_to_9:
            if num in self.cols[x] or num in self.groups[group] or num in self.board[y]:
                continue
            self.board[y][x] = num
            self.groups[group].append(num)
            self.cols[x].append(num)
            if self.try_solving(pos+1):
                return True
            self.groups[group].pop()
            self.cols[x].pop()

        self.board[y][x] = '.'
        return False
    
nums_1_to_9 = set(['1','2','3','4','5','6','7','8','9'])

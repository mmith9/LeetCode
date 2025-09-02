# 5ms on a good day :)
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        board 9x9
        number 1-9 in each row, each column, each 3x3 sub box
        """
        groups =  [[True]*10 for _ in range(10)]    ###
        columns = [[True]*10 for _ in range(10)]    # lookup tables for missing numbers 
        rows =    [[True]*10 for _ in range(10)]    #
        groups_c =  [0 for x in range(9)]   ###
        columns_c = [0 for x in range(9)]   # count blanks for sorting guess order 
        rows_c =    [0 for x in range(9)]   #
        nums_c = [0 for x in range(10)] # count occurences of numbers for sorting 
        blanks = []
       
        for y, row in enumerate(board):
            for x, item in enumerate(row):
                if item == '.':
                    blanks.append((x,y))
                    groups_c[y//3*3 + x//3]+=1
                    columns_c[x]+=1
                    rows_c[y]+=1
                else:
                    num = int(item)
                    nums_c[num] +=1
                    groups[y//3*3 + x//3][num] = False
                    columns[x][num] = False
                    rows[y][num] = False

#        nums_1_to_9 = [7,6,5,1,3,8,4,2,9] # can be as afast as 6ms if sorting is off
#        nums_1_to_9 = [7,8,9,1,2,3,4,5,6]
        nums_1_to_9 = [1,2,3,4,5,6,7,8,9]
        nums_1_to_9.sort(key=lambda x:nums_c[x])

        max_pos = len(blanks)
        blanks.sort(key=lambda x:min(rows_c[x[1]], columns_c[x[0]], groups_c[x[1]//3*3 + x[0]//3]))

        def try_solving(pos) -> bool:
            if pos >= max_pos:
                return True
            x,y = blanks[pos]
            group = groups[y//3*3 + x//3]
            col = columns[x]
            row = rows[y]

            #further optimization possible using bit masks instead of array of true/false
            for num in nums_1_to_9:
                if col[num] and row[num] and group[num]:
                    row[num] = False; col[num] = False; group[num] = False
                    if try_solving(pos+1):
                        board[y][x] = str(num)
                        return True
                    row[num] = True; col[num] = True; group[num] = True
            return False
        
        try_solving(0)

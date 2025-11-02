from typing import List
#Hint1 : brute force it :D
#optimized brute force, faster than 97% 
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        line = [0]*n
        board = [line.copy() for _ in range(m)]
        for row, col in walls:
            board[row][col] = 2
        for row, col in guards:
            board[row][col] = 2
        for row, col in guards:
            the_row = board[row]
            for x in range(col+1, n):
                if the_row[x] == 2:
                    break
                the_row[x] = 1
            for x in range(col-1, -1, -1):
                    if the_row[x] == 2:
                        break
                    the_row[x] = 1
            for x in range(row+1, m):
                if board[x][col] == 2:
                    break
                board[x][col] = 1
            for x in range(row-1, -1, -1):
                if board[x][col] == 2:
                    break
                board[x][col] = 1
        return m*n - sum(sum(row) for row in board) + len(walls) + len(guards)
    


engine = Solution()
m = 4; n = 6; guards = [[0,0],[1,1],[2,3]]; walls = [[0,1],[2,2],[1,4]]
print(engine.countUnguarded(m,n,guards,walls), 7)

m = 3; n = 3; guards = [[1,1]]; walls = [[0,1],[1,0],[2,1],[1,2]]
print(engine.countUnguarded(m,n,guards,walls), 4)



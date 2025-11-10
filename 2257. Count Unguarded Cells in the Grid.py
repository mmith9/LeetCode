from typing import List
#Hint1 : brute force it :D
#optimized brute force, beats 100%
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0]*n for _ in range(m)]
        for row, col in walls:
            board[row][col] = 2
        for row, col in guards:
            board[row][col] = 2
        for row, col in guards:
            the_row = board[row]
            iter = col +1
            while iter != n and the_row[iter]!=2:
                the_row[iter] = 1
                iter+=1
            iter = col -1
            while iter != -1 and the_row[iter]!=2:
                    the_row[iter] = 1
                    iter -= 1
            iter = row +1
            while iter != m and board[iter][col] !=2:
                board[iter][col] = 1
                iter += 1
            iter = row -1
            while iter != -1 and board[iter][col] !=2:
                board[iter][col] = 1
                iter -= 1
        return m*n - sum(sum(row) for row in board) + len(walls) + len(guards)
    

engine = Solution()
m = 4; n = 6; guards = [[0,0],[1,1],[2,3]]; walls = [[0,1],[2,2],[1,4]]
print(engine.countUnguarded(m,n,guards,walls), 7)

m = 3; n = 3; guards = [[1,1]]; walls = [[0,1],[1,0],[2,1],[1,2]]
print(engine.countUnguarded(m,n,guards,walls), 4)



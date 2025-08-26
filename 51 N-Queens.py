from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        def try_solving(x, queens):           
            board[queens] = '.'*x + 'Q' + '.'*(n-x-1)
            if queens == 0: #last queen
                results.append(board.copy())
                return
            
            cols.add(x)
            diag1.add(x-queens)
            diag2.add(x+queens)

            j = queens -1
            for i in range(n):
                if i in cols or i-j in diag1 or i+j in diag2:
                    continue
                try_solving(i, queens-1)

            cols.remove(x)
            diag1.remove(x-queens)
            diag2.remove(x+queens)                    
                    
        for x in range(n//2):
            cols = set()
            diag1 = set()
            diag2 = set()
            board = ['.'*n for _ in range(n)]
            try_solving(x, n-1)
        mirrors = []
        for result in results:
            mirror = []
            for row in result:
                mirror.append(row[::-1])
            mirrors.append(mirror)

        if n % 2 == 1:
            cols = set()
            diag1 = set()
            diag2 = set()
            board = ['.'*n for _ in range(n)]
            try_solving(n//2, n-1)

        results.extend(mirrors)
        return results
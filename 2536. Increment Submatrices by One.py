from typing import List

# optimized, beats 99% 
# Using 2D difference array to optimize the range update process
# Each query increments a submatrix by 1
# After processing all queries, we compute the final matrix using prefix sums

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        #queries list of [row1, col1, row2, col2]
        matrix = [[0]*n for _ in range(n)]
        maxx = n - 1
        for r1, c1, r2, c2 in queries:
            matrix[r1][c1] += 1
            if c2 < maxx:
                matrix[r1][c2 + 1] -= 1
            if r2 < maxx:
                matrix[r2 + 1][c1] -= 1
                if c2 < maxx:
                    matrix[r2 + 1][c2 + 1] += 1

        prev_row = [0]*n
        for row in matrix:
            row_sum = 0
            for idx, prev in enumerate(prev_row):
                row_sum += row[idx]
                row[idx] = row_sum + prev
            prev_row = row
        
        return matrix
    

engine = Solution()
n = 3; queries = [[1,1,2,2],[0,0,1,1]]
expected = [[1,1,0],[1,2,1],[0,1,1]]
obtained = engine.rangeAddQueries(n, queries)
for x in range(n):
    print(obtained[x], expected[x])
print(obtained == expected)

n = 2; queries = [[0,0,1,1]]
expected = [[1,1],[1,1]]
obtained = engine.rangeAddQueries(n, queries)
print(obtained == expected)


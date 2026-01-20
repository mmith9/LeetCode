from itertools import accumulate
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        res = 0; lenx = len(mat[0]); leny = len(mat); maxres = min(lenx, leny)
        acc2d = []
        acc2d.append([0] * (lenx+1))
        lastacc = [0] + list(accumulate(mat[0]))
        acc2d.append(lastacc)
        for y, row in enumerate(mat[1:],1):
            acc = [0]
            for x, num in enumerate(row):
                acc.append(num + lastacc[x+1] + acc[-1] - lastacc[x])
            acc2d.append(acc)
            lastacc = acc

        for y in range(leny):
            for x in range(lenx):
                for z in range(res+1, min(lenx-x, leny-y)+1):
                    if threshold < acc2d[y+z][x+z] - acc2d[y][x+z] - acc2d[y+z][x] + acc2d[y][x]:
                        break
                    res = z
                    if res == maxres:
                        return res
        
        return res



engine = Solution()
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]; threshold = 4
print(engine.maxSideLength(mat, threshold),2)

# mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]; threshold = 1
# print(engine.maxSideLength(mat, threshold),0)





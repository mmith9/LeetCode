from typing import List
#beats 100%
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        inf = 10**5; n1=n+1
        left = [inf] * n1; up = left.copy()
        right = [0] * n1; down = right.copy()

        for x,y in buildings:
            if left[y] > x:
                left[y] = x
            if right[y] < x:
                right[y] = x
            if up[x] > y:
                up[x] = y
            if down[x] < y:
                down[x] = y

        res = 0
        for x,y in buildings:
            if left[y] < x < right[y] and up[x] < y < down[x]:
                res += 1
        return res
    


# slow, but possibly memory effective because of sparseness
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        inf = 10**5; left ={}; right = {}; up = {}; down = {}

        for x,y in buildings:
            left[y] = min(x, left.get(y, inf))
            right[y] = max(x, right.get(y, 0))
            up[x] = min(y, up.get(x, inf))
            down[x] = max(y, down.get(x, 0))

        res = 0
        for x,y in buildings:
            if left[y] < x < right[y] and up[x] < y < down[x]:
                res += 1
        return res
    


engine = Solution()


n = 3; buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
print(engine.countCoveredBuildings(n, buildings),1)

n = 3; buildings = [[1,1],[1,2],[2,1],[2,2]]
print(engine.countCoveredBuildings(n, buildings),0)

n = 5; buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
print(engine.countCoveredBuildings(n, buildings),1)

n = 4; buildings = [[2,4],[1,2],[2,1],[4,3],[3,1],[4,2],[1,4],[2,3],[3,2]]
print(engine.countCoveredBuildings(n, buildings),0)


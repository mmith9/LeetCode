from functools import lru_cache
from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(maxsize=None)
        def rec(start:int, end:int)-> int:
            if end-start <2:
                return 0

            v1 = values[start];v2 = values[end]
            if end - start == 2:
                return v1*v2*values[start+1]

            return min([v1*v2*values[x] + rec(x, end) + rec(start, x) for x in range(start+1,end)])
            
        return rec(0, len(values) -1)


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(maxsize=None)
        def recursion(start:int, end:int)-> int:
            if end-start <2:
                return 0

            v1 = values[start]
            v2 = values[end]
            if end - start == 2:
                return v1*v2*values[start+1]

            mins = []
            for x in range(start+1, end):
                mins.append(v1*v2*values[x] + recursion(x, end) + recursion(start, x))
            return min(mins)

        return recursion(0, len(values) -1)


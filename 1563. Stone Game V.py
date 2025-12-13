# There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
# In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
# The game ends when there is only one stone remaining. Alice's score is initially zero.
# Return the maximum score that Alice can obtain.

from functools import lru_cache
from typing import List

# no cache = TLE 62/132
# cache on recu = TLE 62/132
# twincache = TLE 130/132
# barely passes, 8seconds, requires search from the middle optimization
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        lens = len(stoneValue)

        @lru_cache(None)
        def summ(start:int, end:int) -> int:
            return sum(stoneValue[start:end])

        @lru_cache(None)
        def recu(start:int, end:int) -> int: #non inclusive end
            if end-start <2:
                return 0
            
            res = 0
            sum1 = stoneValue[start]
            sum2 = summ(start+1, end)

            for x in range(start+1, end):
           
                if sum1 > sum2:
                    cur_res = sum2 + recu(x, end)
                elif sum1 < sum2:
                    cur_res = sum1 + recu(start, x)
                else:
                    cur_res = max(sum2 + recu(x, end), sum1 + recu(start, x))

                if cur_res > res:
                    res = cur_res

                sum1 += stoneValue[x]
                sum2 -= stoneValue[x]

            return res
        return recu(0, lens)



engine = Solution()

stoneValue = [6,2,3,4,5,5]
print(engine.stoneGameV(stoneValue), 18)

stoneValue = [7,7,7,7,7,7,7]
print(engine.stoneGameV(stoneValue), 28)

stoneValue = [4]
print(engine.stoneGameV(stoneValue), 0)


stoneValue = [39994,3,4,10000,10000,10000,10000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]
print(engine.stoneGameV(stoneValue), 150003)

stoneValue = [4,9000,6,2,5,5,6,8,3,7,3,4,5,2,1,5,1,6,10,10,3,3,9,3,8,5,5,1,6,6,1,3,7,3,7,8,1,9,5,2,3,9,2,1,4,10,2,10,4,5,6,1,8,5,10,10,9,1,2,5,1,1,10,2,6,8,3,5,8,3,9,3,4,8,1,6,8,5,3,7,3,5,1,10,10,4,6,6,8,5,7,4,1,5,10,2,6,7,5,7,8,4,9,5,2,9,3,7,9,10,1,1,4,3,5,8,9,2,6,3,9,8,9,4,4,9,10,3,7,5,3,4,2,9,7,2,3,1,1,4,10,5,1,2,3,2,7,7,1,5,6,2,4,9,6,10,9,7,8,9,3,3,7,7,3,2,10,9,3,4,6,10,10,2,8,6,10,10,6,1,10,5,1,9,3,4,3,7,5,6,9,2,6,2,4,9,1,9,1,4,3,10,3,6,10,6,10,6,3,7,7,2,5,6,9,10,7,6,7,3,3,5,2,9,5,4,10,6,1,9,3,6,3,10,2,6,3,4,1,10,1,4,9,5,10,2,2,4,8,3,3,8,10,2,6,3,8,9,6,6,7,3,7,3,2,1,3,4,3,9,10,7,4,6,7,8,3,3,5,9,8,2,10,4,6,7,2,10,10,2,5,1,7,2,9,9,5,1,10,5,1,1,1,7,8,10,3,1,6,3,7,9,1,10,5,5,2,5,10,8,10,6,6,8,3,6,4,3,6,7,8,1,3,2,1,4,7,7,8,1,1,4,3,3,7,7,7,6,8,8,1,10,6,4,4,9,9,9,2,3,9,2,10,2,2,6,9,9,1,7,8,1,2,7,8,8,10,10,4,10,8,4,1,6,4,3,8,6,1,7,3,2,7,4,3,6,4,3,10,6,10,10,7,5,10,1,6,8,6,6,3,7,8,7,5,6,5,3,1,4,4,8,8,10,7,4,10,10,8,5,9,6,2,7,10,5,7,1,3,5,3,5,7,5,2,10,3,10,4,6,5,6,2,2,4,1,7,1,1,9,7,8,7,5,4,7,4,8,8,1,2,10,6,6,1,6,6,5,8,5,3,5,9,10,6,9,4,10,10,5,4,1,6000,12500,25000,50000,100000,200000,400000,990000]
print(engine.stoneGameV(stoneValue), 1205175)



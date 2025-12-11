from typing import List

# pure dp, beats 99%
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0,n])
        cuts.sort()
        lens =  len(cuts)
        dp = [[0]* lens for _ in range(lens-1)]

        for k in range(2, lens):
            for i in range(lens - k):
                j = i + k
                dp[i][j] = cuts[j] - cuts[i] + min(dp[i][cut] + dp[cut][j] for cut in range(i+1,j))
        return dp[0][-1]
    

engine = Solution()




n = 7; cuts = [1,3,4,5]
print(engine.minCost(n, cuts), 16)

n = 9; cuts = [5,6,1,4,2]
print(engine.minCost(n, cuts), 22)


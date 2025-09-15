from functools import lru_cache
from typing import List
#optimized recursive, by selecting last baloon to pop
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)

        @lru_cache(maxsize = None)
        def rec(start:int, end: int) -> int:
            if end - start <2:
                return 0
            if end-start == 2:
                return nums[start]*nums[start+1]*nums[start+2]
            
            max_score = 0
            coef = nums[start] * nums[end]
            for x in range(start+1, end):
                max_score = max(max_score, rec(start, x) + rec(x, end) + nums[x]*coef)
            return max_score                                              

        return rec(0, len(nums)-1)

engine = Solution()
nums = [3,1,5,8]
print(engine.maxCoins(nums), 167)


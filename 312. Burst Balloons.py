from functools import lru_cache
from typing import List
#optimized recursive, by selecting last baloon to pop
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [x for x in nums if x!=0] #trim zeros
        nums.insert(0,1)
        nums.append(1)

        @lru_cache(maxsize = None)
        def rec(start:int, end: int) -> int:
            if end-start == 2:
                return nums[start]*nums[start+1]*nums[start+2]
            
            max_score = 0
            coef = nums[start] * nums[end]
            for x in range(start+1, end):
                cur_score = rec(start, x) + rec(x, end) + nums[x]*coef
                if cur_score > max_score:
                    max_score = cur_score
            return max_score                                              
        return rec(0, len(nums)-1)

engine = Solution()
nums = [3,1,5,8]
print(engine.maxCoins(nums), 167)




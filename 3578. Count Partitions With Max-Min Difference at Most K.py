from typing import List
from math import factorial
#quick brute
#optimize: sliding window plus minimum, plus maximum
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        inf = 10**10
        last = 0
        res = 0
        nums.append(inf)
        for idx, num in enumerate(nums):
            nmin = min(nums[last,idx+1])
            nmax = max(nums[last,idx+1])
            if nmax - nmin <= k:
                continue

            n = idx - last
            res = res * factorial(n) % mod


        return res
    

engine = Solution()

nums = [9,4,1,3,7]; k = 4
print(engine.countPartitions(nums, k), 6)

[3,3,4]; k = 0
print(engine.countPartitions(nums, k), 2)        

from typing import List

cache = {}

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        if not cache:
            for x in range(1001, 0 ,-1):
                cache[x|(x+1)] = x
        
        for idx, num in enumerate(nums):
            nums[idx] = cache.get(num, -1)
        return nums
    
from typing import List


cache = {}

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def prep_cache(cache):
            for x in range(1001):
                xbitt = x|(x+1)
                if xbitt in cache:
                    cache[xbitt] = min(x, cache[xbitt])
                else:
                    cache[xbitt] = x

        if not cache:
            prep_cache(cache)
        res = []
        for num in nums:
            res.append(cache.get(num, -1))
        return res
    
    
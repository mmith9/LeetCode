from typing import List
#iterative, beats 100%
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sumn = sum(nums)
        if sumn < p:
            return -1
        target = sumn % p
        if not target:
            return 0

        cycle = 0; mods = {0:-1}; res = len(nums)
        for idx, num in enumerate(nums):
            cycle = (cycle + num) % p
            mods[cycle] = idx
            needmod = (cycle - target) % p
            if needmod in mods:
                res = min(res, idx - mods[needmod])

        if res == len(nums):
            return -1
        return res
engine = Solution()


nums = [1,1,1,1,1,6,1,1,1,1,1]; p = 12
print(engine.minSubarray(nums, p), 4)

nums = [3,1,4,2]; p = 6
print(engine.minSubarray(nums, p), 1)

nums = [6,3,5,2]; p = 9
print(engine.minSubarray(nums, p), 2)

nums = [1,2,3]; p = 3
print(engine.minSubarray(nums, p), 0)

nums = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]; p =26
print(engine.minSubarray(nums, p), 3)

nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]; p = 148
print(engine.minSubarray(nums, p), 7)





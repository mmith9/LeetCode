from collections import defaultdict
from typing import List

#iterative sliding window beats 100%
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        sums = [0 for _ in range(k)]
        sm = sum(nums[:k]); sums[0] = sm; res = sm
        idx = 0
        for drop, add in zip(nums[:-k], nums[k:]):
            idx+=1
            if idx >= k:
                idx -= k
            sm += add - drop

            if sums[idx] < 0:
                new_sum = sm
            else:
                new_sum = sm+sums[idx]
            if new_sum > res:
                res = new_sum
            sums[idx] = new_sum
        return res

#brute force, but why did i do it? 
#TLE 649 / 661 
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(list)
        sm = sum(nums[:k]); sums[0].append(sm)
        idx =0
        for drop, add in zip(nums[:-k], nums[k:]):
            idx+=1
            sm += add - drop
            sums[idx%k].append(sm)

        res = sums[0][0]
        for numz in sums.values():
            #bruteforce ;)
            for left in range(len(numz)):
                for right in range(left, len(numz)):
                    cur = sum(numz[left:right+1])
                    if cur > res:
                        res = cur

        return res

engine = Solution()


nums = [1,2]; k = 1
print(engine.maxSubarraySum(nums, k), 3)

nums = [-1,-2,-3,-4,-5]; k = 4
print(engine.maxSubarraySum(nums, k), -10)

nums = [-5,1,2,-3,4]; k = 2
print(engine.maxSubarraySum(nums, k), 4)








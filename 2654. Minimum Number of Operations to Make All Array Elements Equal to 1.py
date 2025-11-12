from math import gcd
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums) - ones

        if gcd(*nums) != 1:
            return -1
        lens = len(nums)+1
        for step in range(2,lens):
            for group in range(lens-step):
                if gcd(*nums[group:group+step]) == 1:
                    return len(nums)+step-2
                
        assert False
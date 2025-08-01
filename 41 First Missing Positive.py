# o(n) time o(1) memory
#
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_x = len(nums)

        for idx, num in enumerate(nums):
            if num < 1:
                nums[idx] = max_x+1
                   
        for num in nums:
            num = abs(num) -1
            if num < max_x:
                nums[num] = - abs(nums[num])

        for idx, num in enumerate(nums):
            if num>0:
                return idx+1
    
        return max_x +1
                
        

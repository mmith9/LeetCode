from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return get_min(nums)
    
def get_min(nums:List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    cut = int(len(nums)/2)
    if nums[cut-1] > nums[cut]:
        return nums[cut]
    if nums[0] > nums[cut -1]:
        return get_min(nums[:cut])
    if nums[cut] > nums[-1]:
        return get_min(nums[cut:])
    return min(get_min(nums[:cut]), get_min(nums[cut:]))

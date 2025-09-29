from bisect import bisect_left
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        lens = len(nums)

        for num1, a in enumerate(nums[:-2]):
            tail = num1 + 2
            for ib in range(num1+1, lens -1):
                b = nums[ib]
                ab = a + b
                while tail < lens and ab > nums[tail] :
                    tail += 1

                diff = tail -ib -1 
                if diff > 0:
                    count += diff

        return count

#bit faster - beats 20%
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        lens = len(nums)

        for num1, a in enumerate(nums[:-2]):
            tail = num1 + 2
            for num2, b in enumerate(nums[num1+1:-1]):
                ab = a + b
                while tail < lens and ab > nums[tail] :
                    tail += 1

                diff = tail -num1 -num2 -2 
                if diff > 0:
                    count += diff

        return count




#accepted but slow - beats 10%
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for num1, a in enumerate(nums[:-2]):
            for num2, b in enumerate(nums[num1+1:-1]):
                idx = bisect_left(nums, a+b, lo=num1+num2+2)
                count += idx - num1-num2-2
        return count

#naive, TLE on 227/241
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for num1, a in enumerate(nums[:-2]):
            for num2, b in enumerate(nums[num1+1:-1]):
                for c in nums[num1+num2+2:]:
                    if a+b>c: #no degenerated triangles so no =
                        count+=1
                    else:
                        break
        return count
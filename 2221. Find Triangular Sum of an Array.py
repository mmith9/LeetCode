#analytical
from math import comb, factorial
from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        lens = len(nums)-1
        
        suma = 0
        for idx, x in enumerate(nums):
            #numeric overflow?
#            fact_2 = int(factorial(lens)/(factorial(idx)*factorial(lens-idx))) 
            fact = comb(lens, idx)
#            if fact != fact_2:
#                print(idx, fact, fact_2)
            suma += fact * x
#        print()
        return suma % 10


#naive
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            new_nums = []
            for idx in range(len(nums)-1):
                new_nums.append((nums[idx] + nums[idx+1])%10)
            nums = new_nums
        return nums[0]
    

      

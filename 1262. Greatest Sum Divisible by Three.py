from typing import List

#iterative, linear complexity, optimized ifs, beats 100%
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mr11 = mr12 = mr21 = mr22 = 10000; res = 0
        for num in nums:
            res += num
            if num < mr12 and num % 3 == 1:
                if num < mr11:
                    mr11, mr12 = num, mr11
                else:
                    mr12 = num
                
            elif num < mr22 and num % 3 == 2:
                if num < mr21:
                    mr21, mr22 = num, mr21
                else:
                    mr22 = num

        if res % 3 == 0:
            return res
        diff = min(mr11, mr21+mr22) if res % 3 == 1 else min(mr21, mr11+mr12)
        if diff<10000:
            return res - diff
        return 0
 

#oportunistic, NlogN complexity because of sort
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maybe_res = sum(nums)
        if maybe_res % 3 == 0:
            return maybe_res
        
        #nope, need to find something small to deduct to make the sum divisible by 3
        # what would it be? (a, or a+b) % 3 == sum % 3
        one_mod = maybe_res %3
        two_mod = 3 - one_mod

        nums.sort()
        ones = [];twos = []; getones= True; gettwos = True
        for num in nums:
            if getones and num %3 == one_mod:
                ones.append(num)
                getones = False
                if not gettwos:
                    break
            elif gettwos and num %3 == two_mod:
                twos.append(num)
                gettwos = len(twos) <2
                if not getones and not gettwos:
                    break

        diff = ones[0] if ones else 0
        if not gettwos:
            twoss = twos[0]+twos[1]
            if diff == 0 or twoss < diff:
                diff = twoss
        
        if diff:
            return maybe_res - diff
        return 0
    


engine = Solution()

nums = [3,6,5,1,8]
print(engine.maxSumDivThree(nums), 18)

nums = [4]
print(engine.maxSumDivThree(nums), 0)

nums = [1,2,3,4,4]
print(engine.maxSumDivThree(nums), 12)
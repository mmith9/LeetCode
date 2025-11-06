from typing import Counter, List

#unoptimized brute force
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        lens = len(nums); res = []; 
        if k>lens:
            k=lens
        
        for i in range(lens-k+1):
            freqs = Counter(nums[i:k+i]).most_common()
            freqs.sort(key = lambda a: (a[1],a[0]), reverse=True)
            sm = sum(a[0]*a[1] for a in freqs[:x])
            res.append(sm)
        return res


engine = Solution()

nums = [1,1,2,2,3,4,2,3]; k = 6; x = 2
print(engine.findXSum(nums,k ,x), [6,10,12])

nums = [3,8,7,8,7,5]; k = 2; x = 2
print(engine.findXSum(nums,k ,x), [11,15,15,15,12])
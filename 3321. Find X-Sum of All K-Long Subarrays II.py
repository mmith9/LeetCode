from collections import defaultdict
from typing import Counter, List


import bisect
from typing import Counter, List

#with bisect, TLE 778
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        lens = len(nums); res = []; 
        if k>lens:
            k=lens
        
        qju = []

        cnts = Counter(nums[:k])
        for key, value in cnts.items():
            qju.append((value, key))
        qju.sort()
        sm = sum(a[0]*a[1] for a in qju[-x:])
        res.append(sm)

        for i in range(0, lens-k):
            discarded = nums[i]
            added = nums[i+k]

            qju.remove((cnts[discarded], discarded))
            cnts[discarded] -= 1 
            if cnts[discarded] >0:
                bisect.insort_left(qju, (cnts[discarded], discarded))

            if cnts[added] > 0:
                qju.remove((cnts[added], added))
            cnts[added] += 1
            bisect.insort_left(qju, (cnts[added], added))

            sm = sum(a[0]*a[1] for a in qju[-x:])
            res.append(sm)
        return res


#gentle force TLE 776/784
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        lens = len(nums); res = []; 
        if k>lens:
            k=lens
        
        cnts = Counter(nums[:k])
        freqs = cnts.most_common()
        freqs.sort(key = lambda a: (a[1],a[0]), reverse=True)
        sm = sum(a[0]*a[1] for a in freqs[:x])
        res.append(sm)

        for i in range(0, lens-k):
            cnts[nums[i]] -=1
            cnts[nums[i+k]] +=1
            freqs = cnts.most_common()
            freqs.sort(key = lambda a: (a[1],a[0]), reverse=True)
            sm = sum(a[0]*a[1] for a in freqs[:x])
            res.append(sm)
        return res

#unoptimized brute force, tle at 774/784
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
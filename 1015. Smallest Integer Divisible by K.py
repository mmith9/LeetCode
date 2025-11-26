from collections import defaultdict
class Solution:
    #length of smallest integer in form of 111111(1) divisible by k
    def smallestRepunitDivByK(self, k: int) -> int:
        cycler = k % 10
        if cycler in [0,2,4,6,8,5]:
            return -1
        lookup = defaultdict(int)
        for tail in range(10):
            for multiplier in range(1,10):
                if (tail + multiplier*cycler) % 10 == 1:
                    lookup[tail] = multiplier
                    break
        res = 0;mem = k

        while True:
            while mem %10 == 1:
                res +=1
                mem = mem//10
            if not mem:
                return res
            
            tail = mem % 10
            multiplier = lookup[tail]
            mem = (mem + k*multiplier) // 10
            res +=1

engine = Solution()

k = 1
print(engine.smallestRepunitDivByK(k),1)

k = 2
print(engine.smallestRepunitDivByK(k),-1)

k = 3
print(engine.smallestRepunitDivByK(k),3)


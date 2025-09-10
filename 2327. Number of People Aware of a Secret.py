from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if delay >= forget:
            return 0

        delay -=1
        ppls = deque([0]*forget)
        ppls[0] = 1
        seeds = 0 

        for _ in range(n-1):
            seeds -= ppls.pop()
            seeds += ppls[delay]
            ppls.appendleft(seeds)
        return sum(ppls) % (10**9 +7)

engine = Solution()

n = 6; delay = 2; forget = 4
print(engine.peopleAwareOfSecret(n,delay,forget), 'o',5)    
n = 4; delay = 1; forget = 3
print(engine.peopleAwareOfSecret(n,delay,forget), 'o',6)
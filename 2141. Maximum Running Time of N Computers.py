from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n == len(batteries):
            return min(batteries)

        juice = sum(batteries)
        if juice // n >= max(batteries):
            return juice // n

        batteries.sort()
        comps = batteries[-n:]
        juice = sum(batteries[:-n])

        last = comps[0]
        for idx, comp in enumerate(comps[1:],1):
            need = idx * (comp - last)
            if need >= juice:
                return last + juice // idx
            last = comp
            juice -= need
        
        return last + juice // n
            


engine = Solution()

n = 2; batteries = [3,3,3]
print(engine.maxRunTime(n, batteries), 4)

n = 2; batteries = [1,1,1,1]
print(engine.maxRunTime(n, batteries), 2)



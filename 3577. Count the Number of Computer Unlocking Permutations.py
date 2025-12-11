# precalculate factorials with modulos that will be used by all calls
from typing import List

facts = [1]
for x in range(1,10**5+1):
    facts.append(facts[-1] * x % 1_000_000_007)

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] >= min(complexity[1:]):
            return 0
        #this is slow 200ms
        #return factorial(len(complexity)-1) % 1_000_000_007

        #this is fast 7ms
        # res = 1
        # for x in range(1, len(complexity)):
        #     res = res * x % 1_000_000_007
        # return res

        #and this is fastest
        return facts[len(complexity) -1]


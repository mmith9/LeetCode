
from typing import List
from bisect import bisect_left
from bisect import bisect_right
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        lenp=len(potions)
        return [lenp - bisect_left(potions, ceil(success/spell)) for spell in spells]
    

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        lenp = len(potions)
        success -= 1
        return [lenp - bisect_right(potions, success//spell) for spell in spells]

engine = Solution()

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

print(engine.successfulPairs(spells, potions, success))


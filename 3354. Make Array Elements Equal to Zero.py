from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        goal = sum(nums)
        is_odd = goal % 2 
        goal = goal //2
        goal2 = goal + is_odd
        starts = 0

        got = 0
        for x in nums:
            got += x
            if got > goal2:
                break
            if not x and got >= goal:
                starts += 2 - is_odd

        return starts

engine = Solution()

nums = [2,0,2,1,0,0,0,0,0,0,0,0,4]
print(engine.countValidSelections(nums))

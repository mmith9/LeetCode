from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        res = 0 
        events.sort(key = lambda x:x[0])
        max_from = [(events[-1][0], events[-1][2])]
        for left, _, value in events[::-1]:
            if value > max_from[-1][1]:
                if max_from[-1][0] == left:
                    max_from.pop()
                max_from.append((left, value))
        events.sort(key = lambda x:[x[1]])

        for left, right, value in events:
            while max_from and max_from[-1][0] <=  right:
                max_from.pop()
            if max_from:
                value += max_from[-1][1]
            if value > res:
                res = value

        return res


engine = Solution()

events = [[1,3,2],[4,5,2],[2,4,3]]
print(engine.maxTwoEvents(events), 4)

events = [[1,3,2],[4,5,2],[1,5,5]]
print(engine.maxTwoEvents(events), 5)

events = [[1,5,3],[1,5,1],[6,6,5]]    
print(engine.maxTwoEvents(events), 8)
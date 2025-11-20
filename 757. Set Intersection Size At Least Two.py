from typing import List
# easy iterative solution, single digit miliseconds
# It actually attempts to construct containing set in greedy manner
# a,b are last used numbers to construct, a<b
# [left, right] is current interval being considered

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1]) #sort by right end of intervals
        a = b = -1 # last two used integers, -1 is bogus non existing
        res = 0
#        set_=set()
        for left, right in intervals:
            if left <= a: # can use both last numbers
                continue
            elif left <= b: # need one new number, and it needs to be as high as possible
                if right == b: 
                    a = b - 1
                else:
                    a, b = b, right
                res += 1
            else: # need two new numbers, also as high as possible
                a, b = right - 1, right
                res += 2 
#            set_.add(a);set_.add(b)
#        print(set_)
        return res    



engine=Solution()

intervals = [[1,3],[3,7],[8,9]]
print(engine.intersectionSizeTwo(intervals), 5)


intervals = [[1,3],[1,4],[2,5],[3,5]]
print(engine.intersectionSizeTwo(intervals), 3)

intervals = [[1,2],[2,3],[2,4],[4,5]]
print(engine.intersectionSizeTwo(intervals), 5)

intervals = [[1,3],[3,7],[5,7],[7,8]]
print(engine.intersectionSizeTwo(intervals), 5)

intervals = [[1,3],[3,7],[5,7],[7,8]]
print(engine.intersectionSizeTwo(intervals), 5)

intervals = [[5,17],[11,18],[8,9],[12,19],[14,15],[3,11],[8,19],[1,5],[7,14],[3,17],[13,15],[5,19],[2,16],[2,18],[2,18],[1,10],[5,17],[9,13],[10,18],[1,19]]
print(engine.intersectionSizeTwo(intervals), 7)


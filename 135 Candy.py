from typing import List
 
class Solution_naive:
    def candy(self, ratings: List[int]) -> int:
        max_x = len(ratings)
        candys = [0 for x in range(max_x)]

        fixset = set([x for x in range(max_x)])
        while fixset:
            kid = fixset.pop()
            if kid -1 >= 0 and ratings[kid-1] < ratings[kid] and candys[kid-1] >= candys[kid]:
                candys[kid] = candys[kid-1]+1
                if kid+1<max_x:
                    fixset.add(kid+1)
                

            if kid +1 < max_x and ratings[kid+1] < ratings[kid] and candys[kid+1] >= candys[kid]:
                candys[kid] = candys[kid+1]+1
                if kid -1 >=0:
                    fixset.add(kid-1)

        count = max_x
        for x in candys:
            count +=x
        return count

class Solution:
    def candy(self, ratings: List[int]) -> int:
        max_x = len(ratings)
        candys = [0 for x in range(max_x)]
        queue = [x for x in range(max_x)]
        queue.sort(key=lambda x:ratings[x])
        count = max_x

        for kid in queue:
            if kid -1 >= 0 and ratings[kid-1] > ratings[kid] and candys[kid-1] <= candys[kid]:
                candys[kid -1] = candys[kid]+1
                
            if kid +1 < max_x and ratings[kid+1] > ratings[kid] and candys[kid+1] <= candys[kid]:
                candys[kid+1] = candys[kid]+1
        
            count+=candys[kid]

        return count

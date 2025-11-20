from typing import List

class Solution:
    # i-th tap can water range [i-ranges[i], i+ranges[i]]
    # important: need to water all area between 0 and n, not only integer points.
    
    #simple iterative over sorted array of ranges
    def minTaps(self, n: int, ranges: List[int]) -> int:
        #first construct proper ranges
        pranges = []
        for idx, range in enumerate(ranges):
            if range:
                pranges.append((idx-range, idx+range))
        pranges.sort()
        needs = 0; first_free = 0; res = 0

        while needs < n:
            best_e = 0
            for s,e in pranges[first_free:]:
                if s <= needs:
                    first_free +=1
                    if e > best_e:
                        best_e = e
                else:
                    break
            if not best_e:
                return -1
            
            res += 1
            needs = best_e
        return res

# alternatively use bisect, to find index, but then need to run max over found items anyway
# #            print(needs, neede, first_free, pranges)
#             idx = bisect_right(pranges, (needs,999999), lo=first_free)

#             if first_free == idx:
#                 return -1
            
#             maxe = max(x[1] for x in pranges[first_free:idx])
            
#             needs = maxe
#             first_free = idx
#             res +=1

        return res
    


engine = Solution()

n = 5; ranges = [3,4,1,1,0,0]
print(engine.minTaps(n, ranges), 1)

n = 3; ranges = [0,0,0,0]
print(engine.minTaps(n, ranges), -1)

n = 7; ranges = [1,2,1,0,2,1,0,1]
print(engine.minTaps(n, ranges), 3)

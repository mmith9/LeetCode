from itertools import combinations
from typing import List, Set

#funny but ultimately slower solution with generators
from heapq import heapify, heappop, heappush
from itertools import combinations
from typing import List, Set

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        def descending_diffs(nums, last_f):
            nums.append(1)
            nums.sort()
            lenn = len(nums)
            heap = [(f - last_f, idx, lenn) for idx, f in enumerate(nums)]
            heapify(heap)

            while heap:
                neg_diff, i, j = heappop(heap)
                yield -neg_diff
                j -= 1
                if j > i:
                    heappush(heap, (nums[i] - nums[j], i, j))

        gen_h = descending_diffs(hFences, m)
        gen_v = descending_diffs(vFences, n)
        h = next(gen_h)
        v = next(gen_v)

        try:
            while h != v:
                if v>h:
                    v = next(gen_v)
                else:
                    h = next(gen_h)
            return (h*h) % 1_000_000_007                        
        except StopIteration:
            return -1




#somewhat optimized
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m]); vFences.extend([1,n])

        if len(hFences) > len(vFences):
            hFences, vFences = vFences, hFences

        combh = set()
#        for a,b in combinations(hFences, 2):
#            combh.add(abs(a-b))
        for idx, a in enumerate(hFences[:-1],1):
            combh.update(abs(a-x) for x in hFences[idx:])
                
        res = 0
        vFences.sort()
        maxv = vFences[-1]
        for idx, a in enumerate(vFences):
            if maxv - a <= res: 
                break
            for b in vFences[idx+1:][::-1]: #iterate backwards for early exit
                vdiff = b-a
                if vdiff <= res:
                    break
                if vdiff in combh:
                    res = vdiff
                    break
        if res:
            return (res*res) % 1_000_000_007
        return -1

#as simple as it gets
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        def get_combs(nums:List[int]) -> Set[int]:
            a_set = set()
            for a,b in combinations(nums, 2):
                a_set.add(abs(a-b))
            return a_set

        hFences.extend([1,m])
        vFences.extend([1,n])

        combh = get_combs(hFences)
        combv = get_combs(vFences)

        comm = combh.intersection(combv)
        if not comm:
            return -1
        return (max(comm) **2) % 1_000_000_007    

engine = Solution()



m = 4; n = 3; hFences = [2,3]; vFences = [2]
print(engine.maximizeSquareArea(m,n,hFences,vFences), 4)

m = 6; n = 7; hFences = [2]; vFences = [4]
print(engine.maximizeSquareArea(m,n,hFences,vFences), -1)



        
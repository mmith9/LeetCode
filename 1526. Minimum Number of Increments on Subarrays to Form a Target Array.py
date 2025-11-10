from heapq import heapify, heappop, heappush
from typing import List

#proper solution
from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = 0
        lx = 0
        for x in target:
            if x<lx:
                ops+=lx-x
            lx=x
        ops+=x

        return ops
    

#deconstruction from heap, slooow
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if target[0] < target[-1]:
            target = target[::-1]
        heap = []; lens = len(target); maxx = lens-1
        l_idx = 0;l_val = target[0]; ops = 0
        
        is_glued_left = True

        for idx, val in enumerate(target):
            if is_glued_left and val < l_val:
                ops += l_val - val
                l_val = val
                continue

            if val != l_val:
                heap.append((-l_val, l_idx, idx-1))
                l_idx = idx
                l_val = val
                is_glued_left = False

        heap.append((-l_val, l_idx, maxx))    
        heapify(heap)
        

        while heap:
            val, left, right = heappop(heap) # reverse stored 

            while heap and heap[0][0] == val and heap[0][1] == right+1:
                _,_,right = heappop(heap)

            to_left = target[left -1] if left > 0 else 0
            to_right = target[right+1] if right < maxx else 0
            neighbor = max(to_left, to_right)
            ops -= val + neighbor
            if neighbor:
                heappush(heap, (-neighbor, left, right))

        return ops
    

engine = Solution()

target = [1,2,3,2,1]
print(engine.minNumberOperations(target), 3)

target = [3,1,1,2]
print(engine.minNumberOperations(target), 4)

target = [3,1,5,4,2]
print(engine.minNumberOperations(target), 7)


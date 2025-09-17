from typing import List
import bisect
from heapq import heapify, heappop, heappush

#heapq and no pop(0) == fast
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) ==1: #only one list, hmpf
            return [nums[0][0],nums[0][0]]
        
        inf = 10**6
        last_el = max([x[0] for x in nums])
        best_range = [-inf, inf]
        range_size = best_range[1] - best_range[0]

        queue = []
        for n, lst in enumerate(nums):
            queue.append((lst[0],0,len(lst)-1, n))  # cur_val, cur_index, max index, list index
        heapify(queue)

        while True:
            first_el, el_idx, max_el_idx, list_idx = heappop(queue)
                        
            if first_el == last_el:
                return [first_el, first_el] #cant be better than that

            if range_size > last_el - first_el:
                best_range = [first_el, last_el]
                range_size = last_el - first_el

            if el_idx == max_el_idx: #end of story
                return best_range

            el_idx += 1
            next_el = nums[list_idx][el_idx]
            if next_el > last_el:
                last_el = next_el
            heappush(queue, (next_el, el_idx, max_el_idx, list_idx))
    

#unoptimized, pop(0) and bisect kills performance, 
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) ==1: #only one list, hmpf
            return [nums[0][0],nums[0][0]]
        
        inf = 10**6
        nums.sort()
        best_range = [-inf, inf]

        while True:
            first_list = nums.pop(0)
            first_el = first_list.pop(0)
            last_el = nums[-1][0]
            
            if best_range[1] - best_range[0] > last_el - first_el:
                best_range = [first_el, last_el]
            if first_el == last_el:
                return [first_el, last_el] #cant be better than that
            if len(first_list) == 0: #end of story
                return best_range
        
            bisect.insort_left(nums, first_list)

        
    
engine=Solution()

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(engine.smallestRange(nums))
print([20,24])
print()

nums = [[1,2,3],[1,2,3],[1,2,3]]

print(engine.smallestRange(nums))
print([1,1])
print()

nums = [[1,3,5,7,9],[2,4,6,8,10]]
print(engine.smallestRange(nums))
print([1,2])
print()

nums = [
    [-89,1,69,89,90,98],
    [-43,-36,-24,-14,49,61,66,69],
    [73,94,94,96],
    [11,13,76,79,90],
    [-40,-20,1,9,12,12,14],
    [-91,-31,0,21,25,26,28,29,29,30],
    [23,88,89],
    [31,42,42,57],
    [-2,6,11,12,12,13,15],
    [-3,25,34,36,39],
    [-7,3,29,29,31,32,33],
    [4,11,14,15,15,18,19],
    [-34,9,12,19,19,19,19,20],
    [-26,4,47,53,64,64,64,64,64,65],
    [-51,-25,36,38,50,54],
    [17,25,38,38,38,38,40],
    [-30,12,15,19,19,20,22],
    [-14,-13,-10,68,69,69,72,74,75],
    [-39,42,70,70,70,71,72,72,73],
    [-67,-34,6,26,28,28,28,28,29,30,31]]

print(engine.smallestRange(nums))
print([13,73])
print()


nums = [[-38,15,17,18],
        [-34,46,58,59,61],
        [-55,-31,-13,64,82,82,83,84,85],
        [-3,63,70,90],
        [2,6,10,28,28,32,32,32,33],
        [-23,82,88,88,88,89],
        [33,60,72,74,75],
        [-5,44,44,57,58,58,60],
        [-29,-22,-4,-4,17,18,19,19,19,20],
        [22,57,82,89,93,94],
        [24,38,45],
        [-100,-56,41,49,50,53,53,54],
        [-76,-69,-66,-53,-27,-1,9,29,31,32,32,32,34],
        [22,47,56],
        [-34,-28,7,44]]

print(engine.smallestRange(nums))
print([18,82])
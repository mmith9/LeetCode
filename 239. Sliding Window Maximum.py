from collections import deque
from heapq import heapify, heappop, heappush
from typing import List

#list instead deque, minimally faster
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = [0]; res = []; qpos = 0

        for idx, x in enumerate(nums[:k]):
            while queue and nums[queue[-1]] <= x:
                queue.pop()
            queue.append(idx)
        res = [nums[queue[0]]]

        for idx, x in enumerate(nums[k:],k):
            if queue[qpos] <= idx-k:
                qpos+=1
            qlen = len(queue) - qpos
            while qlen and nums[queue[-1]] <= x:
                queue.pop()
                qlen -=1
            queue.append(idx)
            res.append(nums[queue[qpos]])
        return res

#index queue, beats 95%
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for idx, x in enumerate(nums[:k]):
            while queue and nums[queue[-1]] <= x:
                queue.pop()
            queue.append(idx)
        res = [nums[queue[0]]]

        for idx, x in enumerate(nums[k:],k):
            if queue[0] <= idx-k:
                queue.popleft()
            while queue and nums[queue[-1]] <= x:
                queue.pop()
            queue.append(idx)
            res.append(nums[queue[0]])
        return res

#queue with tuples
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for idx, x in enumerate(nums[:k]):
            while queue and queue[-1][0] <= x:
                queue.pop()
            queue.append((x,idx))

        res = [queue[0][0]]

        for idx, x in enumerate(nums[k:],k):
            if queue[0][1] <= idx-k:
                queue.popleft()
            while queue and queue[-1][0] <= x:
                queue.pop()
            queue.append((x,idx))
            res.append(queue[0][0])

        return res

#slow, too much heap ops?
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for idx, x in enumerate(nums[:k]):
            heap.append((-x, idx))
        heapify(heap)
        res = [-heap[0][0]]
        for idx, x in enumerate(nums[k:], k):
            heappush(heap, (-x, idx))
            while heap[0][1] <= idx - k:
                heappop(heap)
            res.append(-heap[0][0])
        return res
   

engine = Solution()


nums = [1,3,-1,-3,5,3,6,7]; k = 3
expected = [3,3,5,5,6,7]
result = engine.maxSlidingWindow(nums, k)
if expected == result:
    print('Ok')
else:
    print(expected)
    print(result)
    print()


nums = [1]; k = 1;  expected = [1]
result = engine.maxSlidingWindow(nums, k)
if expected == result:
    print('Ok')
else:
    print(expected)
    print(result)
    print()



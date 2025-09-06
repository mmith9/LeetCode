import bisect
from typing import List

#naive, TLE @591
class Solution_naive:
    def minOperations(self, queries: List[List[int]]) -> int:
        min_ops = 0

        def zero() -> int:
            nonlocal ints
            if ints[-1] == 0:
                return 0
            a = ints.pop()
            b = ints.pop()
            a = a//4
            b = b//4
            bisect.insort_left(ints, a)
            bisect.insort_left(ints, b)
            return 1 + zero()

        for down,top in queries:
            ints = [x for x in range(down, top+1)]
            min_ops += zero()
        return min_ops
    
# optimized analytic, beats 99%
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        #precalc some full buckets for long testcases
        max_bucket = 14; full_buckets = [0]; pow4=[1]
        for bucket in range(1, max_bucket+1):
            pow4.append(pow4[-1]*4)
            full_buckets.append(bucket* pow4[bucket-1] *3)

        # main loop
        max_ops = 0
        for a,b in queries:
            bucket = (a.bit_length()+1)//2
            last_bucket = (b.bit_length()+1)//2
            cur_ops = 0

            if bucket < last_bucket:
                bucket_max = pow4[bucket]
                cur_ops += bucket*(bucket_max - a)
                a = bucket_max
                bucket += 1

            if bucket < last_bucket:                
                for bucket in range(bucket, last_bucket):
                    cur_ops += full_buckets[bucket]
                a = pow4[bucket]
                bucket+=1
            
            cur_ops += bucket*(b - a + 1)
            max_ops += (cur_ops+1)//2
        return max_ops

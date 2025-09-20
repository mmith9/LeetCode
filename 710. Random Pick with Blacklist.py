from functools import lru_cache
from typing import List
from random import random

#using substitution dict
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.max_n = n - len(blacklist) 
        blackset = set(blacklist)
        n -= 1
        self.replace = {}
        for nono in blackset:
            if nono <= self.max_n:
                while n in blackset:
                    n-=1
                self.replace[nono] = n
                n-=1

    def pick(self) -> int:
        a_rnd = int(random() * self.max_n)
        return self.replace.get(a_rnd, a_rnd)
        

#skip using buckets
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.nono = sorted(blacklist)
        len_bl = len(blacklist)
        self.max_n = n - len_bl -1

        if not blacklist:
            self.buckets = []
            return 
        
        if len_bl < 10:
            self.buckets = [self.nono]
            return

        if len_bl < 100:
            bucket_num = len_bl // 10
        elif len_bl < 1000:
            bucket_num = 20
        else:
            bucket_num = int(len_bl**0.5)

        bucket_size = len_bl // bucket_num
        self.buckets = []
        bucket = []
        for x in self.nono:
            bucket.append(x)
            if len(bucket) >= bucket_size:
                self.buckets.append(bucket)
                bucket = []
        if bucket:
            self.buckets.append(bucket)

    def pick(self) -> int:
        a_rnd = randint(0, self.max_n)
        return self.skip_to(a_rnd)

    def skip_to(self, n:int):
        for bucket in self.buckets:
            if n >= bucket[-1]:
                n += len(bucket)
                continue
            
            if n < bucket[0]:
                return n

            for x in bucket:
                if n < x:
                    return n
                n+=1
        return n

#naive, TLE
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.nono = sorted(blacklist)
        self.max_n = n - len(blacklist)-1

    def pick(self) -> int:
        a_rnd = randint(0, self.max_n)
        return self.skip_to(a_rnd)

    #slow here
    @lru_cache(maxsize = None)
    def skip_to(self, n:int):
        for no in self.nono:
            if no > n:
                break
            n+=1
        return n

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
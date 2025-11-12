from collections import defaultdict
from typing import List

# BLITZ, beats most c++ implemenations on leetcode
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        singletons = 0; buckets = defaultdict(list); lens = len(strs)
        for text in strs:
            buckets[len(text)].append(text.count('0'))

        #greedy grab all string of size 1 if can 
        for zeros in buckets[1]:
            if zeros:
                if m>0:
                    singletons +=1; m -=1
            elif n>0:
                singletons +=1; n -=1
        lens -= len(buckets[1])
        buckets.pop(1, None)

        dp = defaultdict(int)
        dp[(m,n)]=0; curmax = 0

        for length in sorted(buckets.keys()):
            for zeros in buckets[length]:
                ones = length - zeros
                lens -=1
                for (prevm, prevn),v in dp.copy().items():
                    if (prevm+prevn)//length + v <= curmax or v+lens < curmax:
                        dp.pop((prevm, prevn))
                        continue

                    newm, newn = prevm - zeros, prevn - ones
                    if newm >= 0 and newn >= 0 and v >= dp[(newm, newn)]:
                        dp[(newm, newn)] = v + 1
                        if v >= curmax:
                            curmax = v+1

        return curmax + singletons


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        got = 0; idx=0
        strs.sort(key=lambda x:len(x))
        #greedy grab all string of size 1 if can
        for text in strs:
            if len(text)!=1:
                break
            idx+=1 #consume
            if text == '1':
                if n>0:
                    got +=1; n -=1
            elif m>0:
                got +=1; m -=1

        limit = m+n; dp = {(0,0): 0}
        for text in strs[idx:]:
            if len(text) > limit:
                break
            zeros = text.count('0')
            ones = len(text) - zeros
            if zeros>m or ones>n:
                continue

            newdp = {}
            for (prevz, prevo),v in dp.items():
                newz, newo = prevz + zeros, prevo + ones
                if newz <= m and newo <= n:
                    oldv = dp.get((newz, newo), 0)
                    if v+1>oldv:
                        newdp[(newz, newo)] = v + 1
            dp.update(newdp)

        return max(dp.values()) + got

#optimized dp with set 99%
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        pairs = []; got = 0
        strs.sort(key=lambda x:len(x))
        #greedy grab all string of size 1 if can
        for text in strs:
            ones = text.count('1')
            zeros = len(text) - ones
            if ones+zeros ==1:
                if zeros == 1 and m>0:
                    got +=1
                    m -=1
                elif ones == 1 and n>0:
                    got +=1
                    n -=1
                continue

            if zeros<=m and ones<=n:
                pairs.append((zeros, ones))
            elif zeros+ones>m+n:
                break

        dp = set([(0, 0, 0)])
        for zeroes,ones in pairs:
            to_add = set()
            for (z, o, t) in dp:
                if z + zeroes <= m and o + ones <=n:
                    to_add.add((z+zeroes, o+ones, t + 1))
            dp |= to_add
        return max([x[-1] for x in dp])+got

#optimized recursion with greedy grab and early discard, beats 97%
class Solution:
    #m is zero limit, n is one limit
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        pairs = []; got = 0
        strs.sort(key=lambda x:len(x))
        #greedy grab all string of size 1 if can
        for text in strs:
            ones = text.count('1')
            zeros = len(text) - ones
            if ones+zeros ==1:
                if zeros == 1 and m>0:
                    got +=1
                    m -=1
                elif ones == 1 and n>0:
                    got +=1
                    n -=1
                continue

            if zeros<=m and ones<=n:
                pairs.append((zeros, ones))

        lens=len(pairs)

        @lru_cache(maxsize = None)
        def recu(pos, m,n) -> int:
            if pos >= lens:
                return 0

            z,o = pairs[pos]
            if z+o > m+n: #sorted by length, no use looking for more 
                return 0
            
            skip = recu(pos+1, m, n)
            if z>m or o>n:
                return skip
            take = 1 + recu(pos+1, m-z, n-o) if z<=m and o<=n else 0
            if take>skip:
                return take
            return skip

        got += recu(0,m,n)
        return got

            




            


engine = Solution()
strs = ["10","0001","111001","1","0"]; m = 5; n = 3
print(engine.findMaxForm(strs, m, n), 4)

strs = ["101000000","1100001010","11101000","011010110","0010001","0011","0111101111"]
m=10; n=11
print(engine.findMaxForm(strs, m, n), 3)
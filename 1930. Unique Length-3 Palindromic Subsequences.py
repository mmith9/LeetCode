class Solution:
    #oneliner (and it's fast too)
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(len(set(s[s.find(c)+1:s.rfind(c)])) for c in set(s)) 
  
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:   
        if len(s) <= 2:
            return 0
        res = 0
        for c in set(s):
            first = s.find(c)
            last = s.rfind(c)
            if last != first:
                res += len(set(s[first + 1:last]))
        return res
    
from collections import defaultdict
#sets are slow, how about bitmasks? meh, it's even slower....
class Solution:
    #this is even slower somehow, but still kinda fast
    def countPalindromicSubsequence(self, s: str) -> int:
        orda = ord('a'); got = {}; pending = {}; full = set(); fullmask = 2**26 -1; finalize = ''
        for c in s:
            for key, value in pending.items():
                bitmask = 1 << (ord(c) - orda)
                if key == c:
                    got[c] = value
                    if value == fullmask:
                        finalize = c
                pending[key] |= bitmask

            if finalize:
                full.add(finalize)
                got.pop(finalize)
                pending.pop(finalize)
                finalize = ''
                
            if c not in pending and c not in full:
                pending[c] = 0
        return sum(x.bit_count() for x in got.values()) + 26*len(full)

class Solution:
    #set solution with early termination, beats 60%
    def countPalindromicSubsequence(self, s: str) -> int:
        #values is [set_closed, set_open, got_2_allready]
        got = defaultdict(set); pending = {}; full = set(); finalize = ''
        for c in s:
            for key, value in pending.items():
                if key == c:
                    got[key].update(value)
                    value.add(c)
                    if len(got[key]) == 26:
                        finalize = key
                value.add(c)

            if finalize:
                full.add(finalize)
                pending.pop(finalize)
                got.pop(finalize)
                finalize = ''

            if c not in pending and c not in full:
                pending[c] = set()
        
        return sum(len(x) for x in got.values()) + 26*len(full)

class Solution:
    #this is even slower somehow
    def countPalindromicSubsequence(self, s: str) -> int:
        orda = ord('a'); got = {}; pending = {}
        for c in s:
            for key, value in pending.items():
                bitmask = 1 << (ord(c) - orda)
                if key == c:
                    got[c] = value
                pending[key] |= bitmask

            if c not in pending:
                pending[c] = 0
        return sum(x.bit_count() for x in got.values())    

class Solution:
    #slow, beats 30%
    def countPalindromicSubsequence(self, s: str) -> int:
        got = {}; pending = {}
        for c in s:
            for key, value in pending.items():
                if key == c:
                    got[key] = value.copy()
                value.add(c)

            if c not in pending:
                pending[c] = set()
        return sum(len(x) for x in got.values())    
engine = Solution()

s = "aabca"
print(engine.countPalindromicSubsequence(s), 3)

s = "adc"
print(engine.countPalindromicSubsequence(s), 0)

s = "bbcbaba"
print(engine.countPalindromicSubsequence(s), 4)



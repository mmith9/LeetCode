class Solution:
    def maxOperations(self, s: str) -> int:
        include = True; ones = 0; res = 0
        for c in s:
            if c == '1':
                ones += 1
                include = True
            elif include:
                res += ones
                include = False
        return res
    
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0; res = 0
        for cur_ones in map(len, (s+' ').split('0')):
            if cur_ones:
                res += ones
                ones += cur_ones
        return res
    

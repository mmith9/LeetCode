class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        for chunk in s.split('0'):
            if chunk:
                lens = len(chunk)
                res += lens*(lens+1)
        return res//2 % (10**9+7)


class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        for chunk in [chunk for chunk in s.split('0') if chunk]:
            lens = len(chunk)
            res += lens*(lens+1)
        return res//2 %1000000007 

class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        for chunk in [chunk for chunk in s.split('0') if chunk]:
            lens = len(chunk)
            res += lens*(lens+1)//2
        return res % (10**9+7)

class Solution:
    def numSub(self, s: str) -> int:
        return sum(len(x)*(len(x)+1) >> 1 for x in s.split('0') if x) %1000000007  
    
class Solution:
    def numSub(self, s: str) -> int:
        return sum(len(x)*(len(x)+1) for x in s.split('0'))//2 % 1000000007  
    
#slow 
class Solution:
    def numSub(self, s: str) -> int:
       return (cnt:=0) or sum(cnt:=cnt+1 if c=='1' else 0 for c in s)%1000000007  
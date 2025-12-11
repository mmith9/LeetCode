from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        # a*a + b*b = c*c
        res = 0
        for a in range(1,n):
            a2 = a*a
            for b in range(a+1, n):
                suspect = sqrt( a2 + b*b )
                if int(suspect) == suspect and suspect <= n:
                    res += 2
        return res

engine = Solution()

n=5
print(engine.countTriples(n), 2)

n=10
print(engine.countTriples(n), 4)


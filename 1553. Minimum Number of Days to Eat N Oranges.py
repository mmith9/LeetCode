# Eat one orange.
# If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
# If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
# Given the integer n, return the minimum number of days to eat n oranges.
from functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def recu(n:int) -> int:
            if n < 3:
                return n
            return 1+min(n%2+recu(n//2), n%3+recu(n//3))
        return recu(n)
    



engine = Solution()

print(engine.minDays(10), 4)
print(engine.minDays(6), 3)
print(engine.minDays(820592), 22)
print(engine.minDays(429), 12)
print(engine.minDays(280), 9)
        
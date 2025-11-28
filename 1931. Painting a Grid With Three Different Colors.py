import time
from functools import lru_cache
from typing import List, Tuple

#beats 33% recursion is always slower than dp
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        m1 = m-1

        @lru_cache(None)
        def generate_combinations(pstate:Tuple[int,...]) -> List[Tuple[int, ...]]:
            combos = []
            def backtrack(current):
                pos = len(current)
                if pos == m:
                    yield tuple(current)
                    return
                
                for num in (1,2,3):
                    if (not current or current[-1] != num) and (pstate[pos] != num): 
                        yield from backtrack(current + [num])

            for combo in backtrack([]):
                combos.append(combo)
            return combos

        @lru_cache(None)
        def recu(pstate:Tuple[int, ...], cols) -> int:
            if cols <=0:
                return 1
            res = 0

            for state in generate_combinations(pstate):
                res += recu(state, cols-1)
            return res % 1000_000_007
        
        state = [0]*m
        return recu(tuple(state), n)

engine = Solution()

m=1;n=1
print(engine.colorTheGrid(m,n),3)

m=1;n=2
print(engine.colorTheGrid(m,n),6)

m=5;n=5
print(engine.colorTheGrid(m,n),580986)




start = time.perf_counter()
m=5;n=5
print(engine.colorTheGrid(m,n),580986)
end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")

start = time.perf_counter()
m=5;n=900
print(engine.colorTheGrid(m,n),64652768)
end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")


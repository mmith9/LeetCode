from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        max_s = len(s) -1
        max_t = len(t) -1

        @lru_cache(maxsize=None)
        def count_distinct(pos_s, pos_t) -> int:
            if pos_s>max_s or pos_t>max_t or max_s - pos_s < max_t - pos_t:
                return 0
            
            pos_l = s[pos_s:].find(t[pos_t])
            if pos_l <0:
                return 0
            
            next_pos = pos_s + pos_l +1
            if pos_t == max_t:
                count =1
            else:
                count = count_distinct(next_pos, pos_t+1)
            count += count_distinct(next_pos, pos_t)
            return count
        return count_distinct(0,0)

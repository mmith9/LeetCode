from functools import lru_cache
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        max_x = len(s)

        @lru_cache(maxsize = None)
        def recursion(pos):
            if pos >= max_x:
                return [' ']
            cur_sentences = []
            for y in range(pos+1, max_x+1):
                suspect = s[pos:y]
                if suspect in wordDict:
                    next_sentences = recursion(y)
                    for sentence in next_sentences:
                        cur_sentences.append(f'{suspect} {sentence}'.strip())
            return cur_sentences                
        return recursion(0)
from functools import lru_cache
from typing import List, Set

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # cut into 2 non empty
        # scramble both pieces
        # randomly swap scrambled
        # recursion ends at len of 1
        #cache = {}

        def is_possible(a,b):
            lst = set([x for x in a])
            for letter in b:
                if letter not in lst:
                    return False
                lst.remove(letter)
            return True

        @lru_cache(maxsize=None)
        def scramble(s1, s2):
            if len(s1) == 1:
                return s1 == s2

            if not is_possible(s1, s2):
                return False

            for x in range(1, len(s1)):
                if scramble(s1[:x], s2[:x]) and scramble(s1[x:], s2[x:]):
                    return True
                
                s2x = s2[len(s1)-x:] + s2[:len(s1)-x]
                if scramble(s1[:x], s2x[:x]) and scramble(s1[x:], s2x[x:]):
                    return True
            return False

        return scramble(s1,s2)
                
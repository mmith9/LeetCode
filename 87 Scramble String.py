from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # cut into 2 non empty
        # scramble both pieces
        # randomly swap scrambled
        # recursion ends at len of 1

        @lru_cache(maxsize=None)
        def scramble(s1, s2):
            lens1 = len(s1)
            if lens1 <= 2:
                return (lens1 == 1 and s1 == s2) or (lens1==2 and (s1 == s2 or s1==s2[::-1]))

            a = s1
            for letter in s2:
                if letter not in a:
                    return False
                a = a.replace(letter,'',1)

            for x in range(1, lens1):
                if scramble(s1[:x], s2[:x]) and scramble(s1[x:], s2[x:]):
                    return True
                
                if scramble(s1[:x], s2[lens1-x:]) and scramble(s1[x:], s2[:lens1-x]):
                    return True
            return False

        return scramble(s1,s2)
               
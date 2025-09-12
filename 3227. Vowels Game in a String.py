class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return 0 != (s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u'))

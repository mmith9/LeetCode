from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        lens = len(s)
                
        def find_palindromes_at(index):
            ends = [index]
            first_l = s[index]
            index_1 = index+1
            for idx, letter in enumerate(s[index_1:]):
                if letter == first_l:
                    if is_palindrome(index_1, idx + index): #skip first and last, already cmped
                        ends.append(idx + index_1)
            return ends[::-1]

        @lru_cache(maxsize=None)
        def is_palindrome(idx1, idx2) -> bool:
            lenz = idx2 - idx1 +1
            if s[idx1] * lenz == s[idx1:idx1 + lenz]:
                return True
            for x in range(lenz//2):
                if s[x + idx1] != s[idx2-x]:
                    return False
            return True

        @lru_cache(maxsize=None)
        def recursion(idx1) -> int:
            if is_palindrome(idx1, lens-1):
                return 0
            cur_min = lens - idx1 -1
            if cur_min == 1:
                return 1
            for idx2 in find_palindromes_at(idx1):
                cur_min = min(cur_min, 1+ recursion(idx2+1))
                if cur_min == 1:
                    break
            return cur_min
        return recursion(0)



        # @lru_cache(maxsize=None)
        # def is_palindrome3(idx1, idx2) -> bool:
        #     lens = idx2 - idx1 +1
        #     for x , a in enumerate(s[idx1:idx1+lens]):
        #         if a != s[idx2 - x]:
        #             return False
        #     return True


        # @lru_cache(maxsize=None)
        # def is_palindrome2(idx1, idx2) -> bool:
        #     lens = (idx2 - idx1 +2)//2
        #     for a,b in zip(s[idx1:idx1+lens], s[idx2:idx2-lens:-1]):
        #         if a!=b:
        #             return False
        #     return True
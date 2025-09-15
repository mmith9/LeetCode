from functools import lru_cache
from typing import List

#simple and fast, based on dict lookup
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = set()
        wordrev = {}
        for pos,word in enumerate(words):
            wordrev[word[::-1]] = pos

        for num, word in enumerate(words):
            if not word:
                continue

            for pos in range(len(word)+1):
                left = word[:pos]; right = word[pos:]

                if right in wordrev and left == left[::-1]:
                    pairs.add((wordrev[right], num))

                if left in wordrev and right == right[::-1]:
                    pairs.add((num, wordrev[left]))
        
        return [[x,y] for x,y in pairs if x!=y]

# search by looking for sub-palindromes in a word, beats 66%
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = set()
        worddict = {}
        wordrev = {}
        for pos,word in enumerate(words):
            worddict[word] = pos
            wordrev[word[::-1]] = pos
        
        @lru_cache(maxsize=None)
        def sub_pali_left(s:str) -> List[str]:
            result = [s]
            rend = len(s); lend = rend //2; xor_l = 0; xor_r = 0
            odd = ord(s[lend]) if rend % 2 == 1 else 0
            rstart = lend+1 if odd else lend

            for letter in s[:lend]:
                xor_l ^= ord(letter)
            for letter in s[rstart:]:
                xor_r ^= ord(letter)

            while rstart > 0:
                if xor_r == xor_l:
                    if s[:lend] == s[rstart:rend][::-1]:
                        result.append(s[rend:])
                
                rend -= 1
                discarded = ord(s[rend])
                if odd:
                    rstart -= 1
                    xor_r ^= odd ^ discarded
                    odd = 0
                else:
                    lend -= 1
                    odd = ord(s[lend])
                    xor_l ^= odd
                    xor_r ^= discarded

            return result

        for num, word in enumerate(words):
            if not word:
                continue

            for txt in sub_pali_left(word):
                if txt in wordrev:
                    pos = wordrev[txt]
                    if pos != num:
                        pairs.add((pos, num))

            word_ = word[::-1]
            for txt in sub_pali_left(word_):
                if txt in worddict:
                    pos = worddict[txt]
                    if pos != num:
                        pairs.add((num, pos))

        return [list(x) for x in pairs]
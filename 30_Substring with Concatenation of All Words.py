from typing import List, Set
import itertools

class Solution_1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        permutations : Set[str] = set()
        for perm in itertools.permutations(words):
            concat = ''.join(perm)
            permutations.add(concat)

        seek_len = len(words[0])*len(words)

        indices = []
        for x in range(len(s)-seek_len+1):
            substr = s[x:x+seek_len] 
            if substr in permutations:
                indices.append(x)

        return indices

class Solution_2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_num = len(words)
        seek_len = word_len * word_num
        indices = []
        cache = set()
        for x in range(len(s)-seek_len+1):
            substr = substr = s[x:x+seek_len] 
            if substr in cache:
                indices.append(x)
                continue
            
            words_cp = words.copy()
            perm = ''
            for y in range(word_num):
                chop = substr[y*word_len:(y+1)*word_len]
                if chop not in words_cp:
                    break
                words_cp.remove(chop)
                perm += chop
            else:
                indices.append(x)
                cache.add(perm)
        return indices

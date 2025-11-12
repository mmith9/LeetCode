# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class Master:
    def guess(self, word: str) -> int:
        return 0

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
            
        def textdistance(a:str, b:str) -> int:
            return sum(1 for x in range(6) if a[x]!=b[x])
        
        maxmasks = 2
        masks = [words.pop()]
        while len(masks) < maxmasks:
            cur_dist = 0 ; cur_word = ''
            for word in words:
                dist = sum(textdistance(word, mask) for mask in masks)
                if dist > cur_dist:
                    cur_dist = dist
                    cur_word = word
                if dist == 6*len(masks):
                    break
            masks.append(cur_word)
            words.remove(cur_word)

        dists = []
        for mask in masks:
            dists.append((mask, 6-master.guess(mask)))
            if dists[-1][1] == 0:
                return

        suspects = []
        for word in words:
            for mask, dist in dists:
                if textdistance(word, mask) != dist:
                    break
            else:
                suspects.append(word)

        while suspects:
            suspect = suspects.pop()
            guess_dist = 6 - master.guess(suspect)
            if guess_dist == 0:
                return

            new_list = []
            for word in suspects:
                if textdistance(suspect, word) == guess_dist:
                    new_list.append(word)
            suspects = new_list




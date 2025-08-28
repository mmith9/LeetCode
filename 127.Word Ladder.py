from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return 0
        uwords = set(wordList)
        if endWord not in uwords:
            return 0
        uwords.add(beginWord)
        hops = {word:set() for word in uwords}\
        
        chop = len(endWord) //2

        def prep_hops(word):
            uwords.remove(word)
            for hop in uwords:
                if word[chop:] != hop[chop:] and word[:chop] != hop[:chop]:
                    continue
                dist = 0
                for a,b in zip(word, hop):
                    if a!=b:
                        dist+=1
                        if dist>1:
                            break
                if dist==1:
                    hops[word].add(hop)

        word_map = {}
        words_to_map = []
        mapped_words = []

        def map_word(a):
            if a in mapped_words:
                return            
            mapped_words.append(a)

            if a in uwords:
                prep_hops(a)
            if a not in hops:
                return
            
            cur_dist = word_map[a] +1

            for hop in hops[a]:
                if hop in word_map:
                    word_map[hop] = min(word_map[hop], cur_dist)
                else:
                    word_map[hop] = cur_dist
                if hop not in mapped_words:
                    words_to_map.append(hop)

        word_map[endWord] = 1
        words_to_map = [endWord]
        while words_to_map:
            word = words_to_map.pop(0)
            if word == beginWord:
                break
            map_word(word)

        if beginWord in word_map:
            return word_map[beginWord]
        return 0


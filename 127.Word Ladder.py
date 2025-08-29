from typing import List
#textdistance version
class Solution_1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        uwords = set(wordList)
        if endWord not in uwords:
            return 0
        uwords.add(beginWord)
        uwords.remove(endWord)

        queue = set([endWord])
        level = 2
        while queue:
            next_queue = set()
            for cur_word in queue:
                used_words = set()
                for word in uwords:
                    distance = 0
                    for a,b in zip(cur_word, word):
                        if a!=b:
                            distance+=1
                            if distance >1:
                                break
                    if distance == 1:
                        if word == beginWord:
                            return level
                        next_queue.add(word)
                        used_words.add(word)
                uwords.difference_update(used_words)
            queue = next_queue
            level += 1
        return 0
    
# cycle letter version
class Solution_2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        uwords = set(wordList)
        if endWord not in uwords:
            return 0
        uwords.add(beginWord)
        uwords.remove(endWord)
        lens = len(beginWord)
        queue = set([endWord])
        level = 2
        alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
        while queue:
            next_queue = set()
            for cur_word in queue:
                for pos in range(lens):
                    left = cur_word[:pos]
                    right = cur_word[pos+1:]
                    for letter in alphabet:
                        if f'{left}{letter}{right}' in uwords:
                            if f'{left}{letter}{right}' == beginWord:
                                return level
                            next_queue.add(f'{left}{letter}{right}')
            uwords.difference_update(next_queue)
            queue = next_queue
            level += 1
        return 0

# pattern solution
from collections import defaultdict
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        uwords = set(wordList)
        if endWord not in uwords:
            return 0
        uwords.add(beginWord)
        lens = len(beginWord)
        queue = set([endWord])
        level = 2

        patterns = defaultdict(list)
        for word in uwords:
            for x in range(lens):
                pattern = f'{word[:x]}*{word[x+1:]}'
                patterns[word].append(pattern)
                patterns[pattern].append(word)
        uwords.remove(endWord)

        while queue:
            next_queue = set()
            for cur_word in queue:
                for pattern in patterns[cur_word]:
                    for next_word in patterns[pattern]:
                        if next_word in uwords:
                            if next_word == beginWord:
                                return level
                            next_queue.add(next_word)
            uwords.difference_update(next_queue)
            queue = next_queue
            level += 1
        return 0
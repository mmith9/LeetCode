# cycle letter version
from collections import defaultdict
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        uwords = set(wordList)
        if endWord not in uwords:
            return []
        uwords.add(beginWord)
        hops = defaultdict(list)

        uwords.remove(endWord)
        lens = len(beginWord)
        queue = set([endWord])
        alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
       
        def cycle():
            found = False
            nonlocal queue
            while queue:
                next_queue = set()
                for cur_word in queue:
                    for pos in range(lens):
                        left = cur_word[:pos]
                        right = cur_word[pos+1:]
                        for letter in alphabet:
                            if f'{left}{letter}{right}' in uwords:
                                try_word = f'{left}{letter}{right}'
                                hops[try_word].append(cur_word)
                                if try_word == beginWord:
                                    found = True
                                next_queue.add(try_word)
                if found:
                    return True
                uwords.difference_update(next_queue)
                queue = next_queue
            return False

        def get_paths_from(word):
            paths = []
            if not hops[word]:
                return [[word]]
            for next_word in hops[word]:
                for next_path in get_paths_from(next_word):
                    next_path.insert(0, word)
                    paths.append(next_path)
            return paths

        if cycle():
            paths = get_paths_from(beginWord)
            return paths
        else:
            return []


from typing import List
from collections import defaultdict
#naive, with screening, TLE
class Solution_1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        max_x = len(board[0])
        max_y = len(board)

        uwords = set(words)
        words_found = set()

        board_letters = defaultdict(int)
        for row in board:
            for letter in row:
                board_letters[letter] +=1
        
        bad_words = set()
        for word in uwords:
            word_letters = defaultdict(int)
            for letter in word:
                word_letters[letter] +=1
            for letter in word_letters:
                if word_letters[letter] > board_letters[letter]:
                    bad_words.add(word)
                    break
        uwords.difference_update(bad_words)

        stack = set()
        def find_word_at(x,y,word):
            if x<0 or y<0 or x>= max_x or y>=max_y or (x,y) in stack:
                return False
            if word[0] != board[y][x]:
                return False
            if len(word) == 1:
                return True
            stack.add((x,y))
            tail = word[1:]
            result = find_word_at(x+1,y,tail) or find_word_at(x-1,y,tail) or \
                     find_word_at(x,y+1,tail) or find_word_at(x,y-1,tail) 
            stack.remove((x,y))
            return result

        for x in range(max_x):
            for y in range(max_y):
                for word in uwords:
                    if find_word_at(x,y,word):
                        words_found.add(word)
                uwords.difference_update(words_found)

        return list(words_found)
    
from typing import List
#dict based with trimming
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        max_x = len(board[0])
        max_xx = max_x -1
        max_y = len(board)
        max_yy = max_y -1
        words_found = set()

        tree = {}
        for word in words:
            branch = tree
            for letter in word:
                if letter not in branch:
                    branch[letter] = {}
                branch = branch[letter]
            branch['end'] = word

        def trim_tree(branch, word):
            letter = word[0]
            next_branch=branch[letter]
            if len(word) == 1:
                del next_branch['end']                
            else:
                trim_tree(next_branch, word[1:])
            if not next_branch:
                del branch[letter]

        stack = set()
        def find_word_at(x,y, branch):
            if (x,y) in stack:
                return 
            letter = board[y][x]
            if letter not in branch:
                return 
            branch = branch[letter]
            if 'end' in branch:
                words_found.add(branch['end'])
                trim_tree(tree, branch['end'])
                if not branch:
                    return
            stack.add((x,y))
            if x < max_xx:
                find_word_at(x+1,y, branch)
            if x > 0:
                find_word_at(x-1,y, branch)
            if y < max_yy:
                find_word_at(x,y+1, branch)
            if y > 0:
                find_word_at(x,y-1, branch)
            stack.remove((x,y))

        for x in range(max_x):
            for y in range(max_y):
                find_word_at(x,y, tree)
                
        return list(words_found)
    
    
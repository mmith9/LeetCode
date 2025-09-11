#optimized beats 99% cpu 99% mem
from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        counts = defaultdict(int)

        for letter in vowels:
            count = s.count(letter)
            if count:
                counts[letter] = count
                s = s.replace(letter, '_')

        for letter in vowels:
            s = s.replace('_', letter, counts[letter])

        return s
    
#naive optimized
class Solution:
    def sortVowels(self, s: str) -> str:
        vovels = set(['a','e','i','o','u', 'A','E','I','O','U'])

        no_sort = []
        to_sort = []
        for letter in s:
            if letter in vovels:
                to_sort.append(letter)
                no_sort.append(False)
            else:
                no_sort.append(letter)

        to_sort.sort(reverse=True)
        for num, letter in enumerate(no_sort):
            if not letter:
                no_sort[num] = to_sort.pop()

        return ''.join(no_sort)

# Naive
class Solution:
    def sortVowels(self, s: str) -> str:
        vovels = ['a','e','i','o','u', 'A','E','I','O','U']

        napis = []
        to_sort = []
        for letter in s:
            if letter in vovels:
                to_sort.append(letter)
                napis.append(' ')
            else:
                napis.append(letter)

        to_sort.sort()
        for num, letter in enumerate(napis):
            if letter == ' ':
                napis[num] = to_sort.pop(0)

        return ''.join(napis)


engine = Solution()
s = "lEetcOde"
print(engine.sortVowels(s))
print("lEOtcede")

s = "lYmpH"
print(engine.sortVowels(s))
print("lYmpH")
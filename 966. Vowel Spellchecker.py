from typing import List
#optimized, beats 99%
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#       vowels = 'aeiou'
#       faster mask - use a instead _
#        def mask(s:str) -> str:
#            return s.replace('a','_').replace('e','_').replace('i','_').replace('o','_').replace('u','_')
        
        orig = set(wordlist)
        case_dict = {}
        mask_dict = {}
        for word in wordlist:
            word_l = word.lower()
            if word_l not in case_dict:
                case_dict[word_l] = word
            word_l = word_l.replace('e','a').replace('i','a').replace('o','a').replace('u','a')
            if word_l not in mask_dict:
                mask_dict[word_l] = word

        def resolve(query:str) -> str:
            if query in orig:
                return query
                
            query = query.lower()
            if query in case_dict:
                return case_dict[query]
                
            query = query.replace('e','a').replace('i','a').replace('o','a').replace('u','a')
            if query in mask_dict:
                return mask_dict[query]
            
            return ''
           
        return [resolve(query) for query in queries]
            
            
engine = Solution()            

# wordlist = ["KiTe","kite","hare","Hare"]
# queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

# print(engine.spellchecker(wordlist, queries))
# print(expected)

wordlist = ["KiTe","kite","hare","Hare"]
print('words   ', wordlist)
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
#queries = ["kite","kite","KiTe","Hare","hare","","","KiTe","","KiTe"]
print('queries ', queries)
expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
print('result  ',engine.spellchecker(wordlist, queries))
print('expected' ,expected)



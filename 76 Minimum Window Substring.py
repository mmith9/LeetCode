from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        need = {}
        for char in t:
            if char not in need:
                need[char]=1
            else:
                need[char]+=1
        
        got = {}
        for char in need:
            got[char] = 0

        i = 0
        j = 1
        max_j = len(s)
        solution = ''
        if s[0] in need:
            got[s[0]]+=1

        while True:
            if is_solution(got,need):
                while i<j and s[i] not in need:
                    i+=1

                if not solution or len(solution) > j-i:
                    solution = s[i:j]

                if i>=j:
                    break

                got[s[i]]-=1
                i+=1
           
            else:
                while j<max_j and s[j] not in need:
                    j+=1
                if j >= max_j:
                    break
                got[s[j]]+=1
                j+=1
        
        return solution
                
def is_solution(got:Dict[str,int], need:Dict[str,int]) -> bool:
    for char in need:
        if got[char] < need[char]:
            return False
    return True



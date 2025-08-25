class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = fix_p(p)
        return is_match(s, p)

def fix_p(p):
    new_p = ''
    last_catch = ''
    while p:
        if len(p)>1 and p[1] == '*':
            catch = p[:2]
            if (last_catch and catch == '.*') or last_catch == catch:
                pass
            else:
                new_p += last_catch
            last_catch = catch                
            p=p[2:]

        else:
            new_p += last_catch
            last_catch = ''
            new_p += p[0]
            p = p[1:]
    new_p += last_catch
    return new_p

def is_match(s:str, p:str) -> bool:
    if not p:
        return not s

    next_char = p[0]
    is_multi = len(p)>1 and p[1] == '*'
    if is_multi:
        p=p[2:]
    else:
        p=p[1:]
    
    if not s:
        if not p:
            return is_multi
        elif is_multi:
            return is_match(s, p)
        else:
            return False

    if is_multi:
        if next_char == '.':
            lookup = len(s)
        else:
            lookup = 0
            while lookup < len(s) and s[lookup] == next_char:
                lookup+=1

        for x in range(lookup,-1,-1):
            if is_match(s[x:], p):
                return True
    else:
        if next_char == '.' or next_char == s[0]:
            return is_match(s[1:], p)

    return False

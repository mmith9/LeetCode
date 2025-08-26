class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while p.find('**')>=0:
            p = p.replace('**','*')
        
        last = ''
        words = []
        for letter in p:
            if letter in '?*':
                if last:
                    words.append(last)
                    last = ''
            else:
                last += letter
        if last:
            words.append(last)

        pos_s = 0
        for word in words:
            pos_word = s[pos_s:].find(word)
            if pos_word<0:
                return False
            pos_s += pos_word + len(word)

        max_p = len(p)
        max_s = len(s)
        stack = set()

        def try_matching(pos_s:int, pos_p:int) -> bool:
            if ((pos_s, pos_p)) in stack:
                return False
            stack.add((pos_s,pos_p))
            while pos_s < max_s and pos_p < max_p:
                want = p[pos_p]
                if want == '*':
                    break

                if want == '?' or s[pos_s] == want:
                    pos_p+=1
                    pos_s+=1
                else:
                    return False

            if pos_p >= max_p:
                return pos_s >= max_s
            if pos_s >= max_s:
                return (p[pos_p] == '*') and (pos_p == max_p-1)
            
            for x in range(max_s, pos_s-1, -1):
                if try_matching(x, pos_p+1):
                    return True
            return False

        return try_matching(0, 0)
            
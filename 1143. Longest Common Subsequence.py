#

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        insect = set(text1) & set(text2)
        if len(insect) == 0:
            return 0
        text1 = [c for c in text1 if c in insect]
        text2 = [c for c in text2 if c in insect]

        maxx = len(text1)
        line = [0] * maxx

        for y in range(len(text2)):
            chary = text2[y]
            last_b = 0; a = 0
            for x, charx in enumerate(text1):
                b = line[x]
                if charx == chary:
                    a = last_b + 1
                    line[x] = a                    
                elif b > a:
                    a = b
                else:
                    line[x] = a
                last_b = b
            
        res = line[-1]
        
        return res





engine = Solution()


text1 = "abcde"; text2 = "ace" 
print(engine.longestCommonSubsequence(text1, text2), 3)

text1 = "abc"; text2 = "abc"
print(engine.longestCommonSubsequence(text1, text2), 3)

text1 = "abc"; text2 = "def"
print(engine.longestCommonSubsequence(text1, text2), 0)

text1 = "ezupkr"; text2 = "ubmrapg"
print(engine.longestCommonSubsequence(text1, text2), 2)

text1 = "bsbininm"; text2 = "jmjkbkjkv"
print(engine.longestCommonSubsequence(text1, text2), 1)



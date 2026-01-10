class Solution:
    def minimumDeleteSum(self, text1: str, text2: str) -> int:
        total_value = sum(ord(x) for x in text1+text2)

        insect = set(text1) & set(text2)
        if not insect:
            return total_value
        text1 = [ord(c) for c in text1 if c in insect]
        text2 = [ord(c) for c in text2 if c in insect]

        line = [0] * len(text1)

        for c2 in text2:
            last_b = 0; a = 0
            for x, c1 in enumerate(text1):
                b = line[x]
                if c1 == c2:
                    a = last_b + c1
                                
                if b > a:
                    a = b
                else:
                    line[x] = a
                last_b = b
            
        return total_value - 2*line[-1]





engine = Solution()


text1 = "abcde"; text2 = "ace" 
print(engine.minimumDeleteSum(text1, text2), 3)

text1 = "abc"; text2 = "abc"
print(engine.minimumDeleteSum(text1, text2), 3)

text1 = "abc"; text2 = "def"
print(engine.minimumDeleteSum(text1, text2), 0)

text1 = "ezupkr"; text2 = "ubmrapg"
print(engine.minimumDeleteSum(text1, text2), 2)

text1 = "bsbininm"; text2 = "jmjkbkjkv"
print(engine.minimumDeleteSum(text1, text2), 1)



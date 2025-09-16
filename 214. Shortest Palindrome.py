# blitz using xor
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s

        def find_pali():
            rend = len(s); lend = rend //2; 
            odd = ord(s[lend]) if rend % 2 == 1 else 0
            rstart = lend+1 if odd else lend

            xors = 0
            for byt in [ord(x) for x in s]:
                xors ^= byt
            if odd:
                xors ^= odd

            while True:
                if not xors:
                    if s[:lend] == s[rstart:rend][::-1]:
                        return lend + rstart
                
                rend -= 1
                discarded = ord(s[rend])
                if odd:
                    rstart -= 1
                    xors ^= odd ^ discarded
                    odd = 0
                else:
                    lend -= 1
                    odd = ord(s[lend])
                    xors ^= odd ^ discarded

        return s[find_pali():][::-1] + s


# blitz using sum
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s

        def find_pali():
            rend = len(s); lend = rend //2
            odd = ord(s[lend]) if rend % 2 == 1 else 0
            rstart = lend+1 if odd else lend

            suma = sum([ord(x) for x in s[:lend]]) - sum([ord(x) for x in s[rstart:]])

            while True:
                if not suma:
                    if s[:lend] == s[rstart:rend][::-1]:
                        return lend + rstart
                
                rend -= 1
                discarded = ord(s[rend])
                if odd:
                    rstart -= 1
                    suma += discarded - odd
                    odd = 0
                else:
                    lend -= 1
                    odd = ord(s[lend])
                    suma += discarded - odd

        return s[find_pali():][::-1] + s
    

#fast deque
from collections import deque
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s

        print(s)
        def find_pali():
            nums = [ord(x) for x in s]
            lens = len(nums)
            chop = lens // 2
            odd = nums[chop] if lens % 2 == 1 else 0
            right = deque(nums[chop:][::-1] if not odd else nums[chop+1:][::-1])
            left = deque(nums[:chop])

#            print(nums)
            sum_l = sum(left)
            sum_r = sum(right)

            while True:
#                print(left, sum_l)
#                print(right, sum_r)
#                print('pivot', odd)

                if sum_l == sum_r and left == right:
                    if odd:
                        return len(left)*2+1
                    else:
                        return len(left)*2                
                if odd:
                    right.append(odd)
                    discarded = right.popleft()
                    sum_r += odd - discarded
                    odd = 0
                else:
                    odd = left.pop()
                    sum_l -= odd
                    discarded = right.popleft()
                    sum_r -= discarded

        result = find_pali()
#        print(result)
        return s[result:][::-1] + s

# compact
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        l0 = s[0]
        for x in range(len(s)-1,-1, -1):
            if s[x] == l0 and s[:(x+2)//2] == s[x:(x-1)//2:-1]:
                break
        return s[-1:x:-1] + s
    


engine = Solution()
# s = "aacecaaa"
# print(engine.shortestPalindrome(s))
# print("aaacecaaa")

s = "abcd"
print(engine.shortestPalindrome(s))
print("dcbabcd")
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        k-=1
        chars = [x for x in range(1,n+1)]
        result = ''

        while chars:
            perm_cnt = math.factorial(len(chars)-1)
            pos = int(k/perm_cnt)
            k = k - pos*perm_cnt
            num = chars.pop(pos)
            result += str(num)
        return result



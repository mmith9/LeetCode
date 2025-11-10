#very unoptimal brute forcez``
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        inf = 10**4        
        signed = numerator*denominator <0
        if signed:
            numerator = -numerator    
        left = str(numerator // denominator)
        if signed:
            left = '-'+left
        num = numerator % denominator
        
        if num == 0:
            return str(left)
        
        right = ''
        count = 0
        while num !=0 and count < inf:
            num *= 10
            digits = num // denominator
            num = num % denominator
            right += str(digits)[0]
            count+=1

        if num == 0: #complete division
            return left + '.' + right

        #lets try compressing a string
        lenr = len(right)
        for start in range(lenr//2):

            for x in range(start+1, (lenr - start)//2 + start):
                if right[start] != right[x]:
                    continue

                suspect = right[start:x]
                lens = len(suspect)
                count = 0
                max_rep = (len(right) - start ) // lens -1
                while count <= max_rep and (start+(count)*lens) < len(right) and  right[x + count*len(suspect):].startswith(suspect):
                    count+=1
                
                if count >= max_rep :
                    right = right[:start] + '(' + suspect + ')'
                    return left + '.' + right

        return 'error'
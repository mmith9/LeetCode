#substrings means non empty python slices
#dominant ones means count(1) >= count(0)**2

#1600ms
#lets try combined path of a*0 + b*1
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        sqrts = []

        #quick squares lookup
        for x in range(int(len(s)**0.5)+1):
            sqrts += [x] * ((x+1)*(x+1) - x*x)

        def brute_force_from(start:int) -> int:
            limit = sqrts[lens-start]
            res = ones = zeros = z2 = 0
            for c in s[start:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break
                if z2 <= ones:
                    res += 1
            return res 

        def brute_force_with_leading_ones(start:int, pre1:int) -> int:
            res = (1+pre1)*pre1//2 # count substrings within those ones
            ones = zeros = z2 = 0
            limit = sqrts[lens-start+pre1]
            pre1+=1
            for c in s[start:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break

                if z2 <= ones:
                    res += pre1
                elif z2 <= ones + pre1:
                    res += pre1 + ones -z2

            return res

        def brute_force_with_leading_zeros(start:int, pre0:int) -> int:
            res = 0
            ones = zeros = sq1 = 0
            limit = sqrts[lens-start]
            for c in s[start:]:
                if c == '1':
                    ones +=1
                    sq1 = sqrts[ones]
                else:
                    zeros +=1
                    if zeros > limit:
                        break
                                    
                if sq1 >= zeros + pre0:
                    res += pre0
                elif sq1 >= zeros:
                    res += sq1 - zeros +1
                                
            return res


        def brute_force_with_leading_zeros_then_ones(start:int, pre0:int, pre1:int) ->int:
            res = (1+pre1)*(pre1)//2 # count substrings within those ones
            #given consecutive zeros followed by ones
            for x in range(1, pre0+1):
                if x*x > pre1:
                    break
                res += pre1 - x*x +1

            ones = zeros = z2 = 0; sq1 = sqrts[pre1]
            limit = sqrts[lens-start+pre1]
            for c in s[start:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break

                if z2 > ones + pre1:
                    continue                                    
 
                if z2 <= ones:
                    res += pre1 +1
                else:
                    res += pre1 + ones -z2 +1

                sq1 = sqrts[ones + pre1]
                if sq1 >= zeros + pre0:
                    res += pre0
                elif sq1 > zeros:
                    res += sq1 - zeros 

            return res

        #main loop
        pre1 = pre0 = 0; lastc = ''
        for idx, c in enumerate(s):
            if c == '1':
                pre1 += 1
                lastc = '1'
                continue

            elif lastc != '1':
                pre0 +=1
                lastc = '0'
                continue

            if pre1 <= 1:
                if pre0 <= 1:
                    for x in range(1,1+pre0+pre1):
                        res += brute_force_from(idx-x)
                    pre0 = 1
                else:
                    res += brute_force_with_leading_zeros(idx-1, pre0)
                    pre0 = 1

            elif pre0 <= 1:
                if pre0:
                    res += brute_force_from(idx-pre0-pre1)
                
                res += brute_force_with_leading_ones(idx, pre1)
                pre0 = 0
            else:
                res += brute_force_with_leading_zeros_then_ones(idx, pre0, pre1)
                pre0 = 0

            pre1=0

        #any leftovers?
        res += (1+pre1)*(pre1)//2 # count substrings within those ones
        for x in range(1, pre0+1):
            if x*x > pre1:
                break
            res += pre1 - x*x +1

        return res



#1700ms
#lets try combined path of a*0 + b*1
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        sqrts = []

        #quick squares lookup
        for x in range(int(len(s)**0.5)+1):
            sqrts += [x] * ((x+1)**2 - x**2)

        def brute_force_from(start:int) -> int:
            limit = sqrts[lens-start]
            res = ones = zeros = z2 = 0
            for c in s[start:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break
                if z2 <= ones:
                    res += 1
            return res 

        def brute_force_with_leading_ones(start:int, pre1:int) -> int:
            res = (1+pre1)*pre1//2 # count substrings within those ones
            reses = [0] * (pre1+1)
            ones = zeros = z2 = 0
            limit = sqrts[lens-start+pre1]
            for c in s[start:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break

                if z2 <= ones:
                    reses[0] += 1
                
                elif z2 <= ones + pre1:
                    reses[z2-ones] += 1

            sum = 0

            for res_ in reses:
                sum += res_
                res += sum
            return res

        def brute_force_with_leading_zeros(start:int, pre0:int) -> int:
            res = 0
            reses = [0] * (pre0+1)
            ones = zeros = sq1 = 0
            limit = sqrts[lens-start]
            for c in s[start:]:
                if c == '1':
                    ones +=1
                    sq1 = sqrts[ones]
                else:
                    zeros +=1
                    if zeros > limit:
                        break
                                    
                if sq1 >= zeros + pre0:
                    reses[0] +=1
                elif sq1 >= zeros:
                    reses[pre0 - sq1 + zeros] +=1

            sum = 0
            for res_ in reses:
                sum += res_
                res += sum
            return res


        def brute_force_with_leading_zeros_then_ones(start:int, pre0:int, pre1:int) ->int:
            res = (1+pre1)*(pre1)//2 # count substrings within those ones
            #given consecutive zeros followed by ones
            for x in range(1, pre0+1):
                if x*x > pre1:
                    break
                res += pre1 - x*x +1

            res1 = [0] * (pre1+1)
            res0 = [0] * (pre0)
            ones = zeros = z2 = 0; sq1 = sqrts[pre1]
            limit = sqrts[lens-start+pre1]
            for c in s[start:]:
                if c == '1':
                    ones +=1
                    sq1 = sqrts[ones + pre1]
                else:
                    zeros +=1
                    z2 = zeros*zeros
                    if zeros > limit:
                        break
                                    
                if z2 <= ones:
                    res1[0] += 1
                elif z2 <= ones + pre1:
                    res1[z2-ones] += 1

                if sq1 >= zeros + pre0:
                    res0[0] +=1
                elif sq1 > zeros:
                    res0[pre0 - sq1 + zeros] +=1

            sum = 0
            for res_ in res1:
                sum += res_
                res += sum

            sum = 0
            for res_ in res0:
                sum += res_
                res += sum

            return res


        pre1 = pre0 = 0; lastc = ''
        for idx, c in enumerate(s):
            if c == '1':
                pre1 += 1
                lastc = '1'
                continue

            elif lastc != '1':
                pre0 +=1
                lastc = '0'
                continue
            
            # print(res)
            # print(s,idx,c,pre0,pre1)

            if pre1 <= 1:
                if pre0 <= 1:
                    for x in range(1,1+pre0+pre1):
                        res += brute_force_from(idx-x)
                    pre0 = 1
                else:
                    res += brute_force_with_leading_zeros(idx-1, pre0)
                    pre0 = 1

            elif pre0 <= 1:
                if pre0:
                    res += brute_force_from(idx-pre0-pre1)
                
                res += brute_force_with_leading_ones(idx, pre1)
                pre0 = 0
            else:
                res += brute_force_with_leading_zeros_then_ones(idx, pre0, pre1)
                pre0 = 0

            pre1=0

        # print(res)
        # print(s,idx,c,pre0,pre1)

        res += (1+pre1)*(pre1)//2 # count substrings within those ones
        for x in range(1, pre0+1):
            if x*x > pre1:
                break
            res += pre1 - x*x +1

        return res



# separate paths for multiple ones and zeros
# 2000ms, progress!
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s) -1
        limit = int(lens**0.5)
        same_count = 0
        res = 0
        sqrts = []

        #quick squares lookup
        for x in range(int(len(s)**0.5)+1):
            sqrts += [x] * ((x+1)*(x+1) - x*x)


        for idx, c in enumerate(s):
            if idx<lens and c == s[idx+1]:
                same_count +=1
                continue

            if same_count == 0:
                #original brute path
                ones = zeros = z2 = 0
                for c in s[idx:]:
                    if c == '1':
                        ones +=1
                    else:
                        zeros +=1
                        z2 = zeros*zeros
                        if zeros > limit:
                            break
                    if z2 <= ones:
                        res += 1

            #path for leading ones
            elif c == '1':
                res += (1+same_count)*same_count//2 # count substrings within those ones
                reses = [0] * (same_count+1)
                ones = zeros = z2 = 0
                for c in s[idx:]:
                    if c == '1':
                        ones +=1
                    else:
                        zeros +=1
                        z2 = zeros*zeros
                        if zeros > limit:
                            break
                                        
                    if z2 <= ones:
                        reses[0] += 1
                    elif z2 <= ones + same_count:
                        reses[z2-ones] += 1
                sum = 0
                for res_ in reses:
                    sum += res_
                    res += sum
                same_count = 0

                #path for leading zeros
            else:
                reses = [0] * (same_count+1)
                ones = zeros = sq1 = 0
                for c in s[idx:]:
                    if c == '1':
                        ones +=1
                        sq1 = sqrts[ones]
                    else:
                        zeros +=1
                        z2 = zeros*zeros
                        if zeros > limit:
                            break
                                        
                    if sq1 >= zeros + same_count:
                        reses[0] +=1
                    elif sq1 >= zeros:
                        reses[same_count - sq1 + zeros] +=1

                sum = 0
                for res_ in reses:
                    sum += res_
                    res += sum
                same_count = 0

        return res


#gentler force 3000ms and beats 90% 
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        limit = int(lens**0.5)
        res = 0 ; got1 = 0
        for i in range(lens):
            if s[i] == '1':
                got1 += 1
                continue

            #original bruteforce path when no leading zeros
            if got1 == 0:
                ones = zeros = z2 = 0
                for c in s[i:]:
                    if c == '1':
                        ones +=1
                    else:
                        zeros +=1
                        z2 = zeros*zeros
                        if zeros > limit:
                            break
                    if z2 <= ones:
                        res += 1
            else:
                res += (1+got1)*got1//2
                reses = [0] * (got1+1)
                ones = zeros = z2 = 0
                for c in s[i:]:
                    if c == '1':
                        ones +=1
                    else:
                        zeros +=1
                        z2 = zeros*zeros
                        if zeros > limit:
                            break
                                        
                    if z2 <= ones:
                        reses[0] += 1
                    elif z2 <= ones + got1:
                        reses[z2-ones] += 1
                sum = 0
                for res_ in reses:
                    sum += res_
                    res += sum
                got1 = 0
        
        res += (1+got1)*got1//2
        return res

#gentler force 869 / 881 testcases passed
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        sqrs = [x*x for x in range(len(s)+1)]
        lens = len(s); res = 0
        for i in range(lens):
            ones = zeros = 0
            for idx, c in enumerate(s[i:], i):
                if c == '1':
                    ones +=1
                else:
                    zeros +=1

                if ones % 10 == 0: # sparse checking
                    if sqrs[zeros + lens - idx-1] <= ones: #early success
                        res += lens - idx
                        break
                    if zeros*zeros > ones + lens - idx-1: #early fail
                        break

                if zeros*zeros <= ones:
                    res += 1
        return res

#gentler force 870 / 881 testcases passed
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        limit = int(lens**0.5)
        res = 0
        for i in range(lens):
            ones = zeros = 0
            for idx, c in enumerate(s[i:], i):
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                    if zeros > limit:
                        break
                if zeros*zeros <= ones:
                    res += 1
        return res

#gentler force TLE 867 / 881 testcases passed
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        for i in range(lens):
            ones = zeros = 0
            for c in s[i:]:
                if c == '1':
                    ones +=1
                else:
                    zeros +=1
                if zeros*zeros <= ones:
                    res += 1
        return res

#brute force TLE 784 / 881 testcases passed
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        for i in range(lens):
            for j in range(i+1,lens+1):
                ones = s[i:j].count('1')
                zeros = j-i-ones
                if zeros*zeros <= ones:
                    res += 1
        return res
    

engine = Solution()
s = "00011"
print(engine.numberOfSubstrings(s)== 5)

s = "101101"
print(engine.numberOfSubstrings(s)== 16)

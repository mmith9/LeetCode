#k mirror number is a number that is a palindrome if written in k-base
#ex 5 is 101 in base2

#fast generator with power memory
from typing import Iterator
class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def generate_k_mirrors(k:int) -> Iterator[int]:
            tail = [1]; pivot = True; cycler = [1]; num = 1; k_pow = [1]; k1=k-1
            while True:
                yield num

                idx = 0
                while True:
                    tail[idx] += 1                    
                    if tail[idx] < k:
                        num += cycler[idx]
                        break
                    
                    tail[idx] = 0
                    if idx < len(tail) -1:
                        num -= cycler[idx] * k1
                        idx += 1
                        continue

                    k_pow.append(k**len(k_pow))
                    pivot = not pivot
                    cycler = []
                    mid = len(tail)
                    
                    if pivot:
                        tail.append(1)
                        cycler.append(k_pow[mid])
                        for idx in range(1,mid+1):
                            cycler.append(k_pow[mid+idx] + k_pow[mid-idx])
                    else:
                        tail[-1] = 1
                        for idx in range(mid):
                            cycler.append(k_pow[mid+idx] + k_pow[mid-idx-1])
                    num = cycler[-1]
                    break

        gen = generate_k_mirrors(k)
        gen10 = generate_k_mirrors(10)
        res = 0
        while n > 0:
            suspect1 = next(gen)
            suspect2 = next(gen10)

            while suspect1 != suspect2:
                if suspect1 < suspect2:
                    suspect1 = next(gen)
                else:
                    suspect2 = next(gen10)

            res += suspect1
            n -= 1
        return res
    



#fast generator, beats 97%
from typing import Iterator
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_10_mirror(num:int) -> bool:
            return str(num) == str(num)[::-1]

        def generate_k_mirrors(k:int) -> Iterator[int]:
            tail = [1]; pivot = True; cycler = [1]; num = 1; k1=k-1
            while True:
                #print('yeld', num, tail, pivot, cycler)
                
                yield num

                idx = 0
                while True:
                    tail[idx] += 1
                    num += cycler[idx]
                    if tail[idx] < k:
                        break
                    
                    tail[idx] = 0
                    if idx < len(tail) -1:
                        num -= cycler[idx] * k
                        idx += 1
                        continue

                    pivot = not pivot
                    cycler = []

                    mid = len(tail)
                    if pivot:
                        tail.append(1)
                        cycler.append(k**mid)
                        for idx in range(1,mid+1):
                            cycler.append(k**(mid+idx) + k**(mid-idx))
                    else:
                        tail[-1] = 1
                        for idx in range(mid):
                            cycler.append(k**(mid+idx) + k**(mid-idx-1))
                    num = cycler[-1]
                    break

        gen = generate_k_mirrors(k)
        res = 0
        while n > 0:
            suspect = next(gen)
            if is_10_mirror(suspect):
                res += suspect
                n -= 1
        return res
    

#generate k-mirrors, then check if mirror is base10 mirror
#beats 82%
from typing import Iterator
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_10_mirror(num:int) -> bool:
            return str(num) == str(num)[::-1]

        def generate_k_mirrors(k:int) -> Iterator[int]:
            tail = [1]; pivot = True
            while True:
                num = 0; base = 1
                if pivot:
                    for digit in tail[::-1] + tail[1:]:
                        num += digit*base
                        base *= k
                else:
                    for digit in tail[::-1] + tail:
                        num += digit*base
                        base *= k
                yield num
                
                index = 0
                while True:
                    tail[index] += 1
                    if tail[index] < k:
                        break
                    tail[index] = 0
                    if index < len(tail) -1:
                        index += 1
                        continue
                    pivot = not pivot
                    if pivot:
                        tail.append(1)
                    else:
                        tail[index] = 1
                    break 

        gen = generate_k_mirrors(k)
        res = 0
        while n > 0:
            suspect = next(gen)
            if is_10_mirror(suspect):
                res += suspect
                n -= 1
        return res
    

engine= Solution()

k = 2; n = 5
print(engine.kMirror(k, n), 25)

k = 3; n = 7
print(engine.kMirror(k, n), 499)

k = 7; n = 17
print(engine.kMirror(k, n), 20379000)

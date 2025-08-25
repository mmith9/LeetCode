class Solution:
    def countDigitOne(self, n: int) -> int:
        return count_digit_1(str(n))

def count_digit_1(n:str) -> int:
    head = int(n[0])
    new_n = n[1:]    
    power = len(new_n)

    if not power:
        if head >= 1:
            return 1
        else:
            return 0

    if head == 0:
        result = count_digit_1(new_n)

    elif head == 1:
        result = int(new_n) +1 # all 10^power + new_n
        result += count_digit_1(str(10 ** power -1)) # all numbers smaller than 10^power
        result += count_digit_1(new_n)

    else:
        result = head * count_digit_1(str(10 ** power -1)) # all numbers smaller than head * 10^power
        result += count_digit_1(new_n)
        result += 10 ** power # all 1xxxxx

    return result
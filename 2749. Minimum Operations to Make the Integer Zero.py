#You are given two integers num1 and num2.
#In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.
#Return the integer denoting the minimum number of operations needed to make num1 equal to 0.
#If it is impossible to make num1 equal to 0, return -1.

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1,61):
            diff = num1 - i*num2
            if diff < i:
                return -1
            if diff.bit_count() <= i:
                return i
        return -1
    




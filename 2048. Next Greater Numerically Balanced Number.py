
from collections import Counter

#optimized brute recursion, only a bit slower than combination approach
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        nums = [int(x) for x in str(n)]        
        lens = len(nums)
        limit = min(lens+1, 10)
        counts = Counter(nums)

        def recu(idx:int, isgreater:bool) -> bool:
            if idx >= lens:
                if not isgreater:
                    return False

                for x,y in counts.items():
                    if y!=0 and x!=y :
                        return False
                return True
            
            cur_digit = nums[idx]
            counts[cur_digit] -=1
            if isgreater:
                for x in range(1, limit):
                    nums[idx] = x
                    counts[x] +=1
                    if recu(idx+1, isgreater):
                        return True
                    counts[x] -=1
            else:
                for x in range(cur_digit, limit):
                    nums[idx] = x
                    counts[x] +=1
                    if recu(idx+1, x>cur_digit):
                        return True
                    counts[x] -=1

            nums[idx] = cur_digit
            counts[cur_digit] +=1
            return False

        if nums[0] <= lens:
            if recu(0, False):
                num = sum([x*10**y for y,x in enumerate(nums[::-1])])
                return num

        counts = Counter()
        lens+=1
        nums = []
        limit = min(lens+1, 10)

        digit = 1
        for x in range(lens-1):
            nums.append(digit)
            counts[digit] +=1
            if counts[digit] == digit:
                digit+=1
        digit -=1
        nums.append(digit)
        counts[digit] +=1

        if recu(0, False):
            num = sum([x*10**y for y,x in enumerate(nums[::-1])])
            return num

        return 0
    


engine = Solution()

print(engine.nextBeautifulNumber(1), 22)
print(engine.nextBeautifulNumber(1000), 1333)
print(engine.nextBeautifulNumber(3000), 3133)

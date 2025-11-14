from functools import lru_cache
from typing import List


from typing import Dict, List
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        max_h = sum(rods)//2 # maximum height of one side
        rods.sort()
        def do_dh(rods) -> Dict[int, int]:
            # dh in form of difference between sides : max height
            dh = {0:0}
            for rod in rods:
                limit = max_h - rod
                for diff, height in list(dh.items()):
                    #attach rod to higher side
                    if height <= limit:
                        new_diff = diff + rod
                        if height + rod > dh.get(new_diff, 0):
                            dh[new_diff] = height + rod

                    #attach rod to lower side
                    if height - diff <= limit:
                        if diff >= rod:
                            new_diff = diff - rod
                        else:
                            new_diff = rod - diff
                            height += new_diff
                        if height > dh.get(new_diff, 0):
                            dh[new_diff] = height
            return dh
        
        # split rods into two piles and process separately
        # combine results, two sets of rods with same difference can form a billboard
        left = do_dh(rods[:len(rods)//2])
        right = do_dh(rods[len(rods)//2:])    
        return max(left[key] + right[key] - key for key in left.keys() & right.keys())
    

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        rods.sort(reverse=True)
        lens = len(rods)
        max_h = sum(rods)//2
        best_h = 0
        left_to_use = [0]*(lens+1)
        for i in range(lens-1, -1, -1):
            left_to_use[i] = left_to_use[i+1] + rods[i]

        @lru_cache(None)
        def recu(left, right, rod_num) -> int:
            if left > max_h or right > max_h:
                return 0

            nonlocal best_h
            if left == right > best_h:
                best_h = left

            if left + right + left_to_use[rod_num] < 2*best_h:
                return 0

            if rod_num == lens:
                if left == right:
                    return left
                else:
                    return 0
            
            use_left = recu(left + rods[rod_num], right, rod_num + 1)
            if use_left == max_h:
                return use_left
            use_right = recu(left, right + rods[rod_num], rod_num + 1)
            if use_right == max_h:
                return use_right
            skip = recu(left, right, rod_num + 1)
            if skip == max_h:
                return skip
            return max(use_left, use_right, skip)
        result = recu(0,0,0)
        return result
    
engine = Solution()

rods = [1,2,3,6]
print(engine.tallestBillboard(rods), 6)
rods = [1,2,3,4,5,6]
print(engine.tallestBillboard(rods), 10)
rods = [1,2]
print(engine.tallestBillboard(rods), 0)

rods = [1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]
print(engine.tallestBillboard(rods), 1023)

rods = [221,183,216,208,214,226,188,208,194,197,205,184,204,195,208,176,173]
print(engine.tallestBillboard(rods), 0)

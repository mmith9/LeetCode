from typing import List

#recursive
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        #Fail quick
        last = stones[0]
        for num,stone in enumerate(stones):
            if stone - last > num:
                return False
            last = stone

        index = 0
        step = 1
        self.stones = stones
        self.max_x = len(self.stones) -1 
        self.tried = set()
        return self.can_cross_rec(index, step)

    def can_cross_rec(self, index, step):
        if (index,step) in self.tried:
            return False
        cur_stone = self.stones[index] + step

        try:
            cur_index = self.stones[index:index + step + 1].index(cur_stone) + index
        except:
            return False
        
        if cur_index == self.max_x:
            return True
        self.tried.add((index, step))

        return (
            self.can_cross_rec(cur_index, step+1) 
            or self.can_cross_rec(cur_index, step)
            or (step >1 and self.can_cross_rec(cur_index, step-1)))
        
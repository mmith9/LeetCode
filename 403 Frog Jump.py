from typing import List

#recursive
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) <= 1:
            return True
        pos = 0
        step = 1
        self.tried = set()
        self.stones = stones
        self.stones_set = set(stones)
        self.last_pos = len(self.stones) -1 
        return self.can_cross_rec(pos, step)

    def can_cross_rec(self, pos, step):
        if (pos, step) in self.tried:
            return False
        cur_stone = self.stones[pos] + step
        if cur_stone not in self.stones_set:
            return False

        next_pos = self.stones[pos:].index(cur_stone) + pos
        if next_pos == self.last_pos:
            return True
        self.tried.add((pos,step))
   
        return (
            self.can_cross_rec(next_pos, step+1) 
            or self.can_cross_rec(next_pos, step)
            or (step >1 and self.can_cross_rec(next_pos, step-1)))
        
        


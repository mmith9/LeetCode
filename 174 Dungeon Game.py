from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.max_x = len(dungeon) -1
        self.max_y = len(dungeon[0]) -1
        self.dungeon = dungeon
        self.cache = [[None for y in range(self.max_y +1)] for x in range(self.max_x +1)]
        min_hp = self.get_hp_min_for(0, 0, 0)
        if min_hp <=0:
            return 1-min_hp
        else:
            return 1

    def get_hp_min_for(self, x, y, start_hp):
        if self.cache[x][y]:
            cached_hp, cached_min = self.cache[x][y]
            return cached_min + start_hp - cached_hp

        curr_hp = start_hp + self.dungeon[x][y]
        if x==self.max_x and y == self.max_y:
            return curr_hp
        
        min_x = self.get_hp_min_for(x+1, y, curr_hp) if x<self.max_x else -1000000
        min_y = self.get_hp_min_for(x, y+1, curr_hp) if y<self.max_y else -1000000

        curr_min_hp = min(max(min_x, min_y), curr_hp)
        self.cache[x][y] = (start_hp, curr_min_hp)
        return curr_min_hp


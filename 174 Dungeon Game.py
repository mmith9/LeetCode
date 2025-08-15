from typing import List

#recursive
class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.max_x = len(dungeon) -1
        self.max_y = len(dungeon[0]) -1
        self.dungeon = dungeon
        self.cache = [[-1000000 for y in range(self.max_y +1)] for x in range(self.max_x +1)]
        min_hp = self.get_hp_min_for(0, 0)
        if min_hp < 0:
            return 1-min_hp
        else:
            return 1

    def get_hp_min_for(self, x, y):       
        if self.cache[x][y] > -1000000:
            return self.cache[x][y]

        if x < self.max_x and y < self.max_y:
            curr_min_hp = min(max(self.get_hp_min_for(x+1, y), self.get_hp_min_for(x, y+1)), 0) + self.dungeon[x][y]
        elif x == self.max_x:
            if y == self.max_y:
                curr_min_hp = self.dungeon[x][y]
            else:
                curr_min_hp = min(self.get_hp_min_for(x, y+1), 0) + self.dungeon[x][y]
        else:
            curr_min_hp = min(self.get_hp_min_for(x+1 , y), 0) + self.dungeon[x][y]

        self.cache[x][y] = curr_min_hp
        return curr_min_hp

#iterative
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        max_x = len(dungeon) -1
        max_y = len(dungeon[0]) -1
        dungeon[max_x][max_y] = min(0, dungeon[max_x][max_y])

        for y in range(max_y -1, -1, -1):
            self.do_diag(max_x,y, max_x, max_y, dungeon)

        for x in range(max_x-1, -1, -1):
            self.do_diag(x,0, max_x, max_y, dungeon)

        return 1 - dungeon[0][0]

    def do_diag(self, x, y, max_x, max_y, dungeon):
        while True:
            if y == max_y:
                if x < max_x:
                    dungeon[x][y] = min(0, dungeon[x+1][y] + dungeon[x][y])
                else:
                    dungeon[x][y] = min(0, dungeon[x][y])

            elif x == max_x: # y has to be lower than self.max_y
                dungeon[x][y] = min(0, dungeon[x][y+1] + dungeon[x][y])
                
            else:
                dungeon[x][y] = min(0, max(dungeon[x+1][y] + dungeon[x][y], dungeon[x][y+1] + dungeon[x][y]))

            x-=1
            y+=1
            if x < 0 or y > max_y:
                return


        



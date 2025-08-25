from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        max_y = len(mat) -1
        max_x = len(mat[0]) -1
        x = 0
        y = 0
        result = []
        direction = 1 #x+ y-
        while True:
            result.append(mat[y][x])

            if direction == 1: 
                if y == 0 or x == max_x:
                    if x < max_x:
                        x+=1
                    elif y < max_y:
                        y+=1
                    else:
                        return result
                    direction = -direction
                    continue

            elif x == 0 or y == max_y:
                if y < max_y:
                    y+=1
                elif x < max_x:
                    x+=1
                else:
                    return result
                direction = -direction
                continue
            
            x+=direction
            y-=direction
            


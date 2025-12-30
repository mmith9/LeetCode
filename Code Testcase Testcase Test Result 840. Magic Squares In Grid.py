from typing import List



class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        #v1
        def is_magic(y:int, x:int) -> bool:
            a,b,c = grid[y][x:x+3]
            if a%2 == 1 or b%2 == 0 or c%2 == 1 or a+b+c != 15:
                return False
            d,e,f = grid[y+1][x:x+3] #e is always 5
            if d+f != 10:
                return False
            g,h,j = grid[y+2][x:x+3]
            if g+h+j !=15 or a+d+g !=15 or c+f+j != 15 or a+j !=10 or b+h != 10 or c+g !=10:
                return False
            nums = set([a,b,c,d,e,f,g,h,j])
            if len(nums)!=9 or max(nums)!=9 or min(nums)!=1:
                return False
            
            return True

        res = 0
        for rownum, row in enumerate(grid[1:-1]):
            for colnum, num in enumerate(row[1:-1]):
                if num == 5 and is_magic(rownum, colnum):
                    res += 1
        return res

        

engine = Solution()

grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(engine.numMagicSquaresInside(grid),1)

grid = [[8]]
print(engine.numMagicSquaresInside(grid),0)


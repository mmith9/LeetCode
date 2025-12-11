# You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

# You can place the boxes anywhere on the floor.
# If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
# Given an integer n, return the minimum possible number of boxes touching the floor.


class Solution:
    def minimumBoxes(self, n: int) -> int:
        if n < 4:
            return n

        #first fill corner
        res = 1; base = 1; n-=1

        while True:
            base +=1
            can_add = (base+1)*base //2 

            if can_add <= n:
                res += base
                n -= can_add
            else:
                break

        #then fill line by line
        base = 1
        while n > 0:
            res += 1
            n -= base
            base +=1
        
        return res
    


engine = Solution()

print(engine.minimumBoxes(3),3)
print(engine.minimumBoxes(10),6)


        
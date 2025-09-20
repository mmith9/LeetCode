from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for ast in asteroids:
            if ast > 0: #go right, cant collide to left
                result.append(ast)
                continue

            while result:
                last = result[-1]
                if last < 0: #cant collide
                    result.append(ast)
                    break
                
                if last == -ast: #both destroyed
                    result.pop()
                    break
                
                if last > -ast: # current destroyed
                    break

                result.pop() # last destroyed
            else:
                result.append(ast) #nothing left to left
                
        return result
    

engine = Solution()

asteroids = [5,10,-5]
print(engine.asteroidCollision(asteroids))
print([5,10])
print()

asteroids = [8,-8]
print(engine.asteroidCollision(asteroids))
print([])
print()


asteroids = [10,2,-5]
print(engine.asteroidCollision(asteroids))
print([10])
print()

asteroids = [-2,-1,1,2]
print(engine.asteroidCollision(asteroids))
print([-2,-1,1,2])
print()


from typing import List
from decimal import Decimal, getcontext
getcontext().prec = 26  # float (~16) + 10 extra digits


# screw binary search, devour from bottom method
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        edges = defaultdict(int); target = 0
        for _, d, a in squares:
            edges[d] += a
            edges[d+a] -= a
            target += a*a
        target = target /2
        got = 0; width = 0
        for y,nexty in pairwise(sorted(edges)):
            width += edges[y]
            got += (nexty-y)*width
            if got >= target:
                return nexty - (got - target) / width
              


# ugly solution using binary search as hinted
# problems with float precision
#squares [left, down, sidelen]
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sqs = []
        total = Decimal(0)
        precision = Decimal(10**(-5))
        miny = 10**9
        maxy = -(10**9)
        for _,d,a in squares:
            sqs.append([Decimal(d), Decimal(d+a), Decimal(a)]) #[down, up, sidelen]
            total += Decimal(a*a)
            if d<miny:
                miny = d
            if d+a>maxy:
                maxy = d+a
        target = total/2
        miny = Decimal(miny)
        maxy = Decimal(maxy)

        sqs.sort()
#        print(sqs)

        def target_minus_area_below_y(y):
            diff = target
            
            for down,up,a in sqs:
                if down >= y:
                    return diff
                if up <= y:
                    diff -= a*a
                else:
                    diff -= a*(y-down)
            return diff
            
        jump = (maxy-miny)/2
        y = (sqs[-1][1] + sqs[0][0]) /2

        while True:
            diff = target_minus_area_below_y(y)
#            print(diff, y, jump)
            if abs(diff) < precision:
                break
            if diff < 0:
                y -= jump
            else:
                y += jump
            jump = jump/2
             
#        print(y)
        the_min = sqs[0][1]
        for down, up, _ in sqs:
            if down >=y:
                continue
            if down<y<=up:
                return y
            if up>the_min:
                the_min = up

        return the_min


engine = Solution()

# squares = [[0,0,1],[2,2,1]]
# print(engine.separateSquares(squares), 1.0)

# squares = [[0,0,2],[1,1,1]]
# print(engine.separateSquares(squares), 1.16667)

# squares = [[4,28,1],[27,29,1]]
# print(engine.separateSquares(squares), 29)

# squares = [[8,16,1],[6,15,10]]
# print(engine.separateSquares(squares), 29)

squares = [[522261215,954313664,225462],[628661372,718610752,10667],[619734768,941310679,44788],[352367502,656774918,289036],[860247066,905800565,100123],[817623994,962847576,71460],[691552058,782740602,36271],[911356,152015365,513881],[462847044,859151855,233567],[672324240,954509294,685569]]
print(engine.separateSquares(squares), 29)
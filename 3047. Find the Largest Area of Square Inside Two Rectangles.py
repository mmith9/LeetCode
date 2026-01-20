class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # dst = [(bottomLeft[i][0], bottomLeft[i][1], topRight[i][0],topRight[i][1]) for i in range(len(bottomLeft))]
        dst = []
        for i in range(len(bottomLeft)):
            a,b = bottomLeft[i]
            x,y = topRight[i]
            dst.append((a,b,x,y))

        # dst = [(a,b,c,d) for (a,b),(c,d) in zip(bottomLeft, topRight)]

        dst.sort(key = lambda x : x[0]+x[1])

        res = 0
        for i in range(len(dst)-1):
            a1,b1,c1,d1 = dst[i]
            if c1-a1 <= res or d1-b1 <= res:
                continue
            cur_min = c1+d1-res
            for a2,b2,c2,d2 in dst[i+1:]:
                if a2+b2 >= cur_min:
                    break
                if c2-a2 <= res or d2-b2 <= res:
                    continue
                down = a1 if a1>=a2 else a2
                up = c1 if c1<=c2 else c2
                if up - down <= res:
                    continue
                left = b1 if b1>=b2 else b2
                right = d1 if d1<=d2 else d2
                if right-left <= res:
                    continue
                res = min(up-down, right-left)
                cur_min = c1+d1-res

        return res*res




##########################
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        dst = []
        for i in range(len(bottomLeft)):
            a,b = bottomLeft[i]
            c,d = topRight[i]
            dst.append((a,b,c,d))
        dst.sort(key = lambda x : x[0]+x[1]) #sort squares by distance from (0,0)

        res = 0; i = -1
        while i < len(dst)-2:
            i+=1
            a1,b1,c1,d1 = dst[i]
            if c1-a1 <= res or d1-b1 <= res: # too small to produce anything viable
                continue

            cur_min = c1+d1-res # minimum distance for squares to produce a result
            j = i+1

            while j < len(dst):
                a2,b2,c2,d2 = dst[j]
                if c2-a2 <= res or d2-b2 <= res: # too small to produce anything viable, remove from list
                    dst.pop(j)
                    continue

                if a2+b2 >= cur_min: # this and all other (sorted list) are too far
                    break

                down = a1 if a1>=a2 else a2
                up = c1 if c1<=c2 else c2
                if up - down <= res:
                    j+=1
                    continue

                left = b1 if b1>=b2 else b2
                right = d1 if d1<=d2 else d2
                if right-left <= res:
                    j+=1
                    continue

                res = min(up-down, right-left)
                cur_min = c1+d1-res
                j+=1

        return res*res

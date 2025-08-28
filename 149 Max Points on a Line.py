from typing import List

class Solution_naive:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        uniq_pts = [(x[0],x[1]) for x in points]
        if len(uniq_pts) == 1:
            return len(points)

        uniq_pts_c = {}
        for ax, ay in points:
            if (ax, ay) in uniq_pts_c:
                uniq_pts_c[(ax, ay)] +=1
            else:
                uniq_pts_c[(ax, ay)] =1

        max_pts = 0
        
        while len(uniq_pts) >= 2:
            ax, ay = uniq_pts.pop()
            val = uniq_pts_c[(ax,ay)]
            
            for bx, by in uniq_pts:
                cur_max = val + uniq_pts_c[(bx, by)]
                for cx, cy in uniq_pts:
                    if bx == cx and by == cy:
                        continue

                    if are_inline(ax, ay, bx, by, cx, cy):
                        cur_max+=1

                max_pts = max(max_pts, cur_max)
        return max_pts

def are_inline(ax, ay, bx, by, cx, cy):
    # if (ax == cx and ay == cy) or (bx == cx and by == cy):
    #     return True
    if ax == bx or bx == cx:
        return ax == cx 
    if ay == by or by == cy:
        return ay == cy
    return (ax-bx)/(ay-by) == (bx-cx)/(by-cy)

#geometrical
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        uniq_pts = [(x[0],x[1]) for x in points]
        if len(uniq_pts) == 1:
            return len(points)

        uniq_pts_c = {}
        for ax, ay in points:
            if (ax, ay) in uniq_pts_c:
                uniq_pts_c[(ax, ay)] +=1
            else:
                uniq_pts_c[(ax, ay)] =1

        max_pts = 0
        
        while len(uniq_pts) >= 2:
            ax, ay = uniq_pts.pop()
            count_a = uniq_pts_c[(ax,ay)]
           
            vector_c = {}
            
            for bx, by in uniq_pts:
                if ay == by:
                    vector = 'inf'
                else:
                    vector = (ax-bx)/(ay-by)
                
                if vector in vector_c:
                    vector_c[vector] += uniq_pts_c[(bx,by)]
                else:
                    vector_c[vector] = count_a + uniq_pts_c[(bx,by)]

            cur_max = max([value for value in vector_c.values()])
            max_pts = max(max_pts, cur_max)
                        
        return max_pts

    
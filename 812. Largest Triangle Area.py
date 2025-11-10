from typing import List
from itertools import combinations

from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
#        shoelace formula
#        area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
        return max([abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2 for [x1,y1], [x2,y2], [x3,y3] in combinations(points,3)])


#iterative
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
#        shoelace formula
#        area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
        max_area = 0
        for p1 in range(len(points)-2):
            x1,y1 = points[p1]
            for p2 in range(p1+1,len(points)-1):
                x2,y2 = points[p2]
                for p3 in range(p2+1, len(points)):
                    x3,y3 = points[p3]
                    area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
                    if area > max_area:
                        max_area = area
        return max_area


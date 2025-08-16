
import bisect
from typing import List


class Slot:
    def __init__(self, left, right, top):
        self.left = left
        self.right = right
        self.top = top
    def __lt__(self, other):
        return self.top > other.top or (self.top == other.top and self.right<other.right)
    def __eq__(self, other):
        return self.left == other.left and self.right==other.right and self.top==other.top
    def __repr__(self):
        return f"l {self.left} r {self.right} t {self.top}"

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:            
            rects = rectangles
            if not rects:
                  return False
                        
            rects.sort(key=lambda x:-x[1] + x[0]/100000) # from top to bottom, from left to right

            max_left = min([x[0] for x in rects])
            max_down = min([x[1] for x in rects])
            max_down = rects[-1][1]
            max_right = max([x[2] for x in rects])
            max_up = max([x[3] for x in rects])

            return can_fill2(rects, max_left, max_down, max_right,max_up)

def can_fill2(rects, max_left, max_down, max_right, max_up) -> bool:
    need_slots = [Slot(max_left, max_right, max_down)] #filling from bottom
    while need_slots:
        need_slot = need_slots.pop()
        while need_slots and need_slot.left == need_slots[-1].right and need_slot.top == need_slots[-1].top: # glue adjacent slots if necessary
            need_slot.left = need_slots[-1].left
            need_slots.pop()

        while need_slot and rects:
            rect = rects.pop()

            if need_slot.right != rect[2]: 
                return False
            if need_slot.top != rect[1]:
                return False
            if need_slot.left > rect[0]:
                return False

            if rect[3] < max_up: #not filling to top
                bisect.insort(need_slots, Slot(rect[0], rect[2], rect[3]))

            if need_slot.left < rect[0]:
                need_slot.right = rect[0]
            else:
                need_slot = False
        if need_slot:
            return False
    #No more slots needeed, no collisions or holes
    if rects: # something left
        return False
    return True

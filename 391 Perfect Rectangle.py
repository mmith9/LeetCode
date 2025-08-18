
import bisect
from typing import List


class Slot:
    def __init__(self, left, right, top):
        self.left = left
        self.right = right
        self.top = top
    def __lt__(self, other):
        return self.top > other.top or (self.top == other.top and self.right < other.right)
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right and self.top == other.top


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:            
        rectangles.sort(key=lambda x:-x[1] + x[0]/100000) # from top to bottom, from left to right

        max_left = min([x[0] for x in rectangles])
        _, max_down, max_right, _ = rectangles[-1]
        max_up = max([x[3] for x in rectangles])

        return can_fill2(rectangles, max_left, max_down, max_right,max_up)

def can_fill2(rectangles, max_left, max_down, max_right, max_up) -> bool:
    need_slots = []
    need_slot = Slot(max_left, max_right, max_down)
    
    while need_slot and rectangles:
        r_l, r_d, r_r, r_u = rectangles.pop()

        if need_slot.right != r_r: 
            return False
        if need_slot.top != r_d:
            return False
        if need_slot.left > r_l:
            return False

        if r_u < max_up: #not filling to top
            bisect.insort(need_slots, Slot(r_l, r_r, r_u))

        if need_slot.left < r_l:
            need_slot.right = r_l
        else:
            if need_slots:
                need_slot = need_slots.pop()
                while need_slots and need_slot.left == need_slots[-1].right and need_slot.top == need_slots[-1].top: # glue adjacent slots if necessary
                    need_slot.left = need_slots.pop().left        
            else:
                need_slot = False

    #No more slots needeed, no collisions or holes
    return not rectangles and not need_slot # is something left

import bisect
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
            rects = rectangles
            if not rects:
                  return False
            
            rects.sort(key=lambda x:x[0]) 
            rects.sort(key=lambda x:x[1]) # by left down corner, to down

            max_left = rects[0][0]
            max_down = rects[0][1]
            max_right = rects[0][2]
            max_up = rects[0][3]
            got_area = 0
            corners = []
            for rect in rects:
                max_left = min(rect[0], max_left)
                max_down = min(rect[1], max_down)
                max_right = max(rect[2], max_right)
                max_up = max(rect[3], max_up)
                got_area += (rect[2] - rect[0]) * (rect[3] - rect[1])
                # corners.append((rect[0],rect[1]))
                # corners.append((rect[2],rect[1]))    #no speed gain
                # corners.append((rect[0],rect[3]))
                # corners.append((rect[2],rect[3]))

            if (max_right - max_left) * (max_up - max_down) != got_area: # quick area check for fast fail
                return False

            # for corner in [(max_left, max_down), (max_left, max_up), (max_right, max_down), (max_right, max_up)]:
            #     if corner not in corners:
            #         return False

            return can_fill(rects, max_left, max_down, max_right,max_up)

class Slot:
    def __init__(self, left, right, top):
        self.left = left
        self.right = right
        self.top = top
    def __lt__(self, other):
        return self.top > other.top or (self.top == other.top and self.right<other.right)
    def __eq__(self, other):
        return self.left == other.left and self.right==other.right and self.top==other.top

def can_fill(rects, max_left, max_down, max_right, max_up) -> bool:
    need_slots = [Slot(max_left, max_right, max_down)] #filling from bottom
    while need_slots:

        need_slot = need_slots.pop()
        while need_slots and need_slot.top == need_slots[-1].top and need_slot.left == need_slots[-1].right: # glue adjacent slots if necessary
            need_slot.left = need_slots[-1].left
            need_slots.pop()

        for rect in rects:
            if need_slot.top < rect[1]: #rect is higher than lowest slot, means not filler for slot found
                return False
            if need_slot.top > rect[1]: #rect is below lowest slot, means overlapping
                return False
            if need_slot.left > rect[0]: #rect is colliding with something to left
                continue
            if need_slot.right < rect[2]: #rect is colliding with something to right
                continue
            
            # got fitting rectangle
           
            if rect[3] < max_up: #not filling to top
                bisect.insort(need_slots, Slot(rect[0], rect[2], rect[3]))

            if need_slot.left < rect[0]: #not filling from left
                need_slots.append(Slot(need_slot.left, rect[0], need_slot.top)) # add left gap

            if rect[2] < need_slot.right: #not filling from right
                need_slots.append(Slot(rect[2], need_slot.right, need_slot.top)) # add gap to right

            rects.remove(rect)
            break
        else: # no suitable rects
            return False
   
    #No more slots needeed, no collisions or holes
    if rects: # something left
        return False
    return True
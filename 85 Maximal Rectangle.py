from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_y = len(matrix)

        rangess = []
        max_rect = 0

        for row in matrix:
            ranges = []
            start = -1
            end = -1
            for pos, value in enumerate(row):
                if value == '1':
                    if start <0:
                        start = pos
                    end = pos
                else:
                    if start >=0:
                        ranges.append((start, end))
                        max_rect = max(max_rect, end - start +1)
                        start = -1
            if start >=0:
                ranges.append((start, end))    
                max_rect = max(max_rect, end - start +1)
            rangess.append(ranges)

        def proc_next_line(top_row, cur_row, cur_start, cur_end, max_rect) -> int:
            if cur_row >= max_y:
                return max_rect
            
            if (cur_end - cur_start+1)*(max_y - top_row) <= max_rect:
                return max_rect
            
            ranges = rangess[cur_row]
            for start, end in reversed(ranges):
                if end < cur_start:
                    break
                if start > cur_end:
                    continue

                if start >= cur_start and end <= cur_end: # contained within -> consume
                    ranges.remove((start, end))
                    max_rect = max(max_rect, (end - start +1)*(cur_row - top_row +1),
                        proc_next_line(top_row, cur_row+1, start, end, max_rect))
                    continue
    
                if start <= cur_start and end >= cur_end: # encompassing, 
                    max_rect = max(max_rect, (cur_end - cur_start +1)*(cur_row - top_row +1),
                        proc_next_line(top_row, cur_row+1, cur_start, cur_end, max_rect))
                    break

                if start >= cur_start:
                    max_rect = max(max_rect, (cur_end - start +1)*(cur_row - top_row +1),
                        proc_next_line(top_row, cur_row+1, start, cur_end, max_rect))
                    continue

                if end <= cur_end:
                    max_rect = max(max_rect, (end - cur_start +1)*(cur_row - top_row +1),
                        proc_next_line(top_row, cur_row+1, cur_start, end, max_rect))
                    break

                assert False
            return max_rect

        for y in range(max_y):
            ranges = rangess[y]
            while ranges:
                start, end = ranges.pop()
                max_rect = max(max_rect, proc_next_line(y, y+1, start, end, max_rect))
        return max_rect

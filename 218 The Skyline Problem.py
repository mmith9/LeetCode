from typing import List

# INVALID
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        buildings.sort(key=lambda x:x[0])
        map = []
        while buildings:
            item = buildings.pop(0)
            if item[0] >= item[1]:
                continue

            for next in buildings:
                if next[0]>=next[1]:
                    continue
                if item[1] < next[0]:
                    continue

                if item[2] < next[2]:
                    item[1] = next[0]

                elif item[2] > next[2]:
                    next[0] = item[1]

            if item[0] >= item[1]:
                continue
            map.append(item)
                
        result = []
        map.sort(key=lambda x:x[0])
        while map:
            item = map.pop(0)
            while map and item[1]>=map[0][0] and item[2] == map[0][2]:
                item[1] = max(item[1], map[0][1])
                map.pop(0)

            result.append((item[0],item[2]))
            if map:
                if item[1] < map[0][0]:
                    result.append((item[1], 0))
            else:
                result.append((item[1], 0))

        return result
    


buildings = [[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]

engine = Solution()
print(engine.getSkyline(buildings))
from collections import defaultdict
from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0]*numberOfUsers
        mention_all = 0
        offlines = defaultdict(list)
        
        for msg, time, id in events:
            if msg == 'OFFLINE':
                offlines[int(id)].append(int(time))
        
        for msg, time, ids in events:
            if msg == 'MESSAGE':
                for id in ids.split():
                    if id=='ALL':
                        mention_all+=1

                    elif id!='HERE':
                        res[int(id[2:])] += 1

                    else: #now processing HERE
                        time = int(time)
                        for id, num in enumerate(res):
                            for off in offlines.get(id, []):
                                if off <= time < off + 60:
                                    break
                            else:#not on break
                                res[id] = num + 1
        if mention_all:
            for id, num in enumerate(res):
                res[id] = num + mention_all
        return res
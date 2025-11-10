from typing import List
import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task2prio = {}
        self.task2user = {}
        self.rmed = set()
        # tasks = list[userId, taskId, priority]
        for userId, taskId, priority in tasks:
            self.heap.append((-priority, -taskId, userId))
            self.task2prio[taskId] = priority
            self.task2user[taskId] = userId
        
        heapq.heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        if taskId in self.rmed:
            self.rmed.discard(taskId)
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.task2prio[taskId] = priority
        self.task2user[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task2user[taskId]
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))
        self.task2prio[taskId] = newPriority
        
    def rmv(self, taskId: int) -> None:
        self.rmed.add(taskId)

    def execTop(self) -> int:
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            taskId = -taskId
            if taskId in self.rmed:
                continue
            if self.task2prio[taskId] != -priority: #stale
                continue
            if self.task2user[taskId] != userId: # bad entry
                continue
            
            self.rmed.add(taskId)
            return userId
        return -1
    

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

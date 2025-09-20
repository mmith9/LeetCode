from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List


#bisecting deque is slow for some reason, this is better
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List


#bit faster
class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.queues = defaultdict(list)
        self.queue_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.queue_set:
            return False

        if len(self.queue) >= self.limit:
            packet_to_rm = self.queue.popleft()
            self.queues[packet_to_rm[1]].pop(0)
            self.queue_set.remove(packet_to_rm)
        
        self.queue.append(packet)
        self.queue_set.add(packet)
        self.queues[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.queues[packet[1]].pop(0)
        self.queue_set.remove(packet)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        queue = self.queues[destination]
        left = bisect_left(queue, startTime)
        right = bisect_right(queue, endTime)
        return right - left
    
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


#bit faster
class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.queues = defaultdict(deque)
        self.queue_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.queue_set:
            return False

        if len(self.queue) >= self.limit:
            dst = self.queue.popleft()
            src, tim = self.queues[dst].popleft()
            self.queue_set.discard((src, dst, tim))
        
        self.queue.append(destination)
        self.queue_set.add(packet)
        self.queues[destination].append((source, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        destination = self.queue.popleft()
        source, timestamp = self.queues[destination].popleft()
        self.queue_set.remove((source, destination, timestamp))
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        queue = self.queues[destination]
        left = bisect_left(queue, startTime, key=lambda x:x[1])
        right = bisect_right(queue, endTime, key=lambda x:x[1])
        return right - left
    
    
#naive, TLE
class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.queue_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.queue_set:
            return False

        if len(self.queue) >= self.limit:
            self.queue.popleft()
        
        self.queue.append(packet)
        self.queue_set.add(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.queue_set.remove((source, destination, timestamp))
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        
        left = bisect_left(self.queue, startTime, key=lambda x:x[2])
        right = bisect_right(self.queue, endTime, key=lambda x:x[2])
        count = sum([1 for x in range(left, right) if self.queue[x][1] == destination])
        return count
    
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
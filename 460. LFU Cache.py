from collections import defaultdict, deque
class LFUCache:
    
    def __init__(self, capacity: int):
        self.key2val = {}
        self.key2freq = {}
        self.freq2key_q = defaultdict(deque)
        self.free = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1

        freq = self.key2freq[key]
        self.freq2key_q[freq].remove(key)
        if len(self.freq2key_q[freq]) == 0:
            del self.freq2key_q[freq]
            if freq == self.min_freq:
                self.min_freq +=1
        freq += 1
        self.key2freq[key] = freq
        self.freq2key_q[freq].append(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.free == 0 and key not in self.key2val:
            least_used = self.min_freq
            to_del = self.freq2key_q[least_used].popleft()
            if not self.freq2key_q[least_used]:
                del self.freq2key_q[least_used]

            del self.key2val[to_del]
            del self.key2freq[to_del]
            freq = 1  
            self.min_freq = 1
        elif key not in self.key2val:
            freq = 1
            self.min_freq = 1
            self.free -= 1
        else:
            freq = self.key2freq[key]
            self.freq2key_q[freq].remove(key)
            if not self.freq2key_q[freq]:
                del self.freq2key_q[freq]
                if freq == self.min_freq:
                    self.min_freq+=1
            freq += 1

        self.key2val[key] = value
        self.key2freq[key] = freq
        self.freq2key_q[freq].append(key)



#kinda slow
import bisect
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.keys = []
        self.free = capacity
        self.seq = 0

    def get(self, key: int) -> int:
        self.seq += 1
        if key not in self.cache:
            return -1
        entry = self.cache[key]
        entry['uses'] += 1
        entry['last_access'] = self.seq
        self.keys.remove(key)
        bisect.insort_left(self.keys, key, key = lambda x: (-self.cache[x]['uses'], -self.cache[x]['last_access']))
        return entry['value']

    def put(self, key: int, value: int) -> None:
        self.seq+=1
        if self.free == 0 and key not in self.cache:
            to_del = self.keys.pop()
            del self.cache[to_del]
            self.free += 1

        if key in self.cache:
            uses = self.cache[key]['uses'] + 1
            self.keys.remove(key)
        else:
            uses = 1
            self.free -= 1

        entry = {'uses':uses, 'last_access':self.seq, 'value':value}
        self.cache[key] = entry
       
        bisect.insort_left(self.keys, key, key = lambda x: (-self.cache[x]['uses'], -self.cache[x]['last_access']))




            # keys = [x for x in self.cache.keys()]
            # keys.sort(key = lambda x:(self.cache[x]['uses'], self.cache[x]['last_access']), reverse=True)
            # to_del = keys.pop()
            # del self.cache[to_del]
            # self.free += 1

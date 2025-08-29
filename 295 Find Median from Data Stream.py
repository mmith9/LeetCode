from bisect import insort
# solution that keeps values that not fit in the bucket
class MedianFinder_1:
    def __init__(self):
        self.left = []
        self.buckets = [0 for _ in range(101)]
        self.bucket_fill = 0
        self.right = []

    def addNum(self, num: int) -> None:
        if 0 <= num <= 100 :
            self.buckets[num]+=1
            self.bucket_fill+=1
        elif num < 0:
            insort(self.left, num)
        else:
            insort(self.right, num)

    def getNum(self, idx:int):
        lenr = len(self.right)
        lenl = len(self.left)
        total = self.bucket_fill + lenr + lenl

        if idx < lenl:
            return self.left[idx]
        elif idx >= self.bucket_fill + lenl:
            return self.right[idx - lenl - self.bucket_fill]
        else:
            got_elems = lenl
            for num, count in enumerate(self.buckets):
                if idx < got_elems + count:
                    return num
                else:
                    got_elems += count
            assert False

    def findMedian(self) -> float:
        lenl = len(self.left)
        lenr = len(self.right)

        totals = self.bucket_fill + lenl + lenr
        if totals % 2 == 1:
            return self.getNum(totals//2)
        else:
            return (self.getNum(totals//2-1) + self.getNum(totals//2))/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# dynamic bucket
from bisect import insort, bisect_left
class MedianFinder:
    def __init__(self):
        self.buckets = {}
        self.bucket_fill = 0
        self.keys = []
        self.class_fil = {}
        self.class_keys = []
        self.class_width = 100

    def addNum(self, num: int) -> None:
        if num not in self.buckets:
            self.buckets[num] = 0
            insort(self.keys, num)
        self.buckets[num]+=1
        self.bucket_fill+=1
        if num>=0:
            num_class = int(num/self.class_width)*self.class_width
        else:
            num_class = int((num-self.class_width+1)/self.class_width)*self.class_width
        if num_class not in self.class_fil:
            self.class_fil[num_class] = 0
            insort(self.class_keys, num_class)
        self.class_fil[num_class] +=1

    def getNum(self, idx:int):
        got_elems = 0
        start_index = 0
        for key in self.class_keys:
            class_elems = self.class_fil[key]
            if idx >= got_elems + class_elems:
                got_elems += class_elems
            else:
                start_index = bisect_left(self.keys, key)
                break

        for key in self.keys[start_index:]:
            got_elems += self.buckets[key]
            if idx < got_elems:
                return key
        return 0 

    def findMedian(self) -> float:
        totals = self.bucket_fill
        if totals % 2 == 1:
            return self.getNum(totals//2)
        else:
            return (self.getNum(totals//2-1) + self.getNum(totals//2))/2

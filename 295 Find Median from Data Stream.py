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


# solution that discards values that not fit in the bucket
class MedianFinder:
    def __init__(self):
        self.left = 0
        self.buckets = [0 for _ in range(101)]
        self.bucket_fill = 0
        self.right = 0

    def addNum(self, num: int) -> None:
        if 0 <= num <= 100 :
            self.buckets[num]+=1
            self.bucket_fill+=1
        elif num < 0:
            self.left +=1            
        else:
            self.right +=1

    def getNum(self, idx:int):
        lenl = self.left
        assert idx >= lenl
        assert idx < self.bucket_fill + lenl

        got_elems = lenl
        for num, count in enumerate(self.buckets):
            if idx < got_elems + count:
                return num
            else:
                got_elems += count
        assert False

    def findMedian(self) -> float:
        totals = self.bucket_fill + self.left + self.right
        if totals % 2 == 1:
            return self.getNum(totals//2)
        else:
            return (self.getNum(totals//2-1) + self.getNum(totals//2))/2

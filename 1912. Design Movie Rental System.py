from bisect import insort_left
from collections import defaultdict
from typing import List



class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]): #[shop, movie, price]
        self.pricing = [defaultdict(int) for _ in range(n)]
        self.free = defaultdict(list)
        self.rented = []

        for shop, movie, price in entries:
            self.pricing[shop][movie] = price
            self.free[movie].append((price,shop))

        for frez in self.free.values():
            frez.sort()

    def search(self, movie: int) -> List[int]:
        available = [ shop for _, shop in self.free[movie][:5]]
        return available

    def rent(self, shop: int, movie: int) -> None:
        price = self.pricing[shop][movie]
        insort_left(self.rented, (price, shop, movie))
        self.free[movie].remove((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.pricing[shop][movie]
        self.rented.remove((price, shop, movie))
        insort_left(self.free[movie], (price, shop))

    def report(self) -> List[List[int]]:
        first_5 = [[id, movie] for price, id, movie in self.rented[:5]]
        return first_5



["MovieRentingSystem","search","rent","rent","report","drop","search"]
#[1],
# [0,1],
# [1,2],
# [],
# [1,2],
# [2]]
engine = MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]) #shop movie price
print('search 1', engine.search(1))
engine.rent(0, 1)
engine.rent(1,2)
print('report', engine.report())
engine.drop(1,2)
print('report',engine.report())

print('expected: [1,0,2] [[0,1], [1,2]] [0,1]]')

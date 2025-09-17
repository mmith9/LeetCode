from collections import defaultdict
from typing import List

from bisect import insort_left
from collections import defaultdict
from typing import List
import heapq

from heapq import heapify, heappush, heappop
#using heapq, even faster
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2r = defaultdict(list)
        self.f2c = {}
        self.f2r = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2r[food] = rating
            self.f2c[food] = cuisine
            self.c2r[cuisine].append((-rating, food))
        for heap in self.c2r.values():
            heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        self.f2r[food] = newRating
        heappush(self.c2r[self.f2c[food]], (-newRating, food))        

    def highestRated(self, cuisine: str) -> str:
        heap = self.c2r[cuisine]
        while heap:
            rating, food = heap[0]
            if self.f2r[food] == -rating:
                return food
            heappop(heap) #stale rating
        assert False # wrong input only

#using sorted set from sorted containers, 20x faster than bisect and list
from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2f = defaultdict(SortedSet)
        self.f2c = {}
        self.f2r = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2r[food] = rating
            self.f2c[food] = cuisine
            self.c2f[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        a_set = self.c2f[cuisine]
        a_set.remove((-self.f2r[food], food))
        self.f2r[food] = newRating
        a_set.add((-self.f2r[food], food))

    def highestRated(self, cuisine: str) -> str:
        return self.c2f[cuisine][0][1]

#same as below, but the key for sorting is external table instead direct in list
#and this is somehow 2x faster?
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2f = defaultdict(list)
        self.f2c = {}
        self.f2r = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2r[food] = rating
            self.f2c[food] = cuisine
            self.c2f[cuisine].append(food)
        for queue in self.c2f.values():
            queue.sort(key=lambda food:(-self.f2r[food], food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        queue = self.c2f[cuisine]
        queue.remove(food)
        self.f2r[food] = newRating
        insort_left(queue, food, key=lambda food:(-self.f2r[food], food))

    def highestRated(self, cuisine: str) -> str:
        return self.c2f[cuisine][0]

from bisect import insort_left
from collections import defaultdict
from typing import List
import heapq

#using bisect, kinda slow but passes tests
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2f = defaultdict(list)
        self.f2c = {}
        self.f2r = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2r[food] = rating
            self.f2c[food] = cuisine
            self.c2f[cuisine].append((-rating, food))
        for queue in self.c2f.values():
            queue.sort()

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        queue = self.c2f[cuisine]
        queue.remove((-self.f2r[food], food))
        self.f2r[food] = newRating
        insort_left(queue, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.c2f[cuisine][0][1]

# simple, TLE on 73 of 78 ineffective max probably
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c2f = defaultdict(list)
        self.f2c = {}
        self.f2r = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2c[food] = cuisine
            self.c2f[cuisine].append(food)
            self.f2r[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        self.f2r[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return min([food for food in self.c2f[cuisine]], key = lambda x:(-self.f2r[x], x))
      

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
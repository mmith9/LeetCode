#better brute TLE 17/30
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lens = len(stations)
        powers = []

        for idx in range(lens):
            powers.append(sum(stations[max(0, idx-r):idx+r+1]))
        
        while k:
            minp = min(powers)
            idx = powers.index(minp)
            powers[idx] += k
            nextmin = min(powers)
            powers[idx] -= k
            diff = nextmin - minp
            if not diff:
                diff = 1
            for x in range(idx, min(lens, idx+r+r+1)):
                powers[x]+=diff
            k-=diff
        return min(powers)

#brute TLE 16/30
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lens = len(stations)
        powers = []

        for idx, station in enumerate(stations):
            powers.append(sum(stations[max(0, idx-r):idx+r+1]))
        
        while k:
            minp = min(powers)
            idx = powers.index(minp)
            for x in range(idx, min(lens, idx+r+r+1)):
                powers[x]+=1
            k-=1
        
        return min(powers)
engine = Solution()

stations = [1,2,4,5,0]; r = 1; k = 2
print(engine.maxPower(stations, r, k), 5)

stations = [4,4,4,4]; r = 0; k = 3
print(engine.maxPower(stations, r, k), 4)





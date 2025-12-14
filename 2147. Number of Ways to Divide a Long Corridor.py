class Solution:
    def numberOfWays(self, corridor: str) -> int:
        #fail quick
        seats = corridor.count('S')
        if seats <2 or seats % 2 == 1:
            return 0

        #consume leading plants and one seat
        idx = 0
        for a in corridor:
            idx+=1
            if a == 'S':
                break

        #now we can't have zero seats, so just toggle a bool
        res = 1; seats = False; plants = 1
        for a in corridor[idx:]:
            if a == 'P':
                if seats:
                    plants += 1
            elif seats:
                if plants > 1:
                    res = res * plants % 1_000_000_007
                seats = False
                plants = 1
            else:
                seats = True
                
        return res
    

engine=Solution()


corridor = "SSPPSPS"
print(engine.numberOfWays(corridor), 3)

corridor = "PPSPSP"
print(engine.numberOfWays(corridor), 1)

corridor = "S"
print(engine.numberOfWays(corridor), 0)

corridor = "SPPSSSSPPS"
print(engine.numberOfWays(corridor), 1)

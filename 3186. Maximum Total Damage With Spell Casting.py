class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        blasts = Counter(power)
        indices = sorted(blasts.keys())

        @lru_cache(maxsize=None)
        def recu(start, end):
            if start == end:
                dmg = indices[start]
                return blasts[dmg]*dmg
            max_dmg = 0

            start3 = min(start+3, end+1)
            start_dmg = indices[start]
            for idx in range(start, start3):
                dmg = indices[idx]
                if dmg > start_dmg+2:
                    break
                cur_dmg = blasts[dmg] * dmg

                right = idx +1
                while right <= end and indices[right] <= dmg+2:
                    right+=1
                if right <= end:
                    cur_dmg += recu(right, end)

                if cur_dmg > max_dmg:
                    max_dmg = cur_dmg
            return max_dmg

        result = 0
        left = 0
        lastd = indices[0]
        for x, dmg in enumerate(indices):
            if lastd +2 < dmg:
                result += recu(left, x-1)
                left = x
            lastd = dmg
        result += recu(left, len(indices)-1)
        return result
    





engine = Solution()

power = [1,1,3,4]
print(engine.maximumTotalDamage(power), 6)

power = [7,1,6,6]

print(engine.maximumTotalDamage(power), 13)

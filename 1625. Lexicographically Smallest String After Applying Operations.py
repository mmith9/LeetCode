from collections import defaultdict
#blitz, beats 100%
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        #a is modulo 10 cycler for all odd
        #b is rotator to right
        lens = len(s)

        moduler = {}
        moduler[0] = (0, 0)
        for num in range(1, 10):
            cur_min = num
            moduler[num] = (num, 0)
            for rots in range(1, 10):
                num_rot = (num + a*rots) % 10
                if num_rot == num:
                    break
                if num_rot in moduler:
                    moduler[num] = (moduler[num_rot][0], moduler[num_rot][1] + rots)
                    break

                if num < cur_min:
                    cur_min = num
                    moduler[num] = (cur_min, rots)

        can_rot_even = b % 2 == 1
        base_list = [int(x) for x in s]

        def get_rolled_list(idx, even_r, odd_r):
            new_list = []
            for x in range(lens):
                cur_rot = even_r if x % 2 == 0 else odd_r
                new_list.append((base_list[(idx+x) % lens] + a*cur_rot) % 10)
            return new_list

        used = set()
        cur_best = base_list.copy()
        idx = 0
        while idx not in used:
            used.add(idx)

            _, even_r = moduler[base_list[idx]] if can_rot_even else (0,0)
            _, odd_r = moduler[base_list[(idx+1) % lens]]

            for x in range(lens):
                cur_rot = even_r if x % 2 == 0 else odd_r
                cur_num = (base_list[(idx+x)%lens] + cur_rot*a) % 10
                if cur_num < cur_best[x]:
                    cur_best = get_rolled_list(idx, even_r, odd_r)
                if cur_num > cur_best[x]:
                    break
            
            idx = (idx + b) % lens

        return ''.join([str(x) for x in cur_best])


engine = Solution()

# s = "5525"; a = 9; b = 2
# print(engine.findLexSmallestString(s,a,b), "2050")


# s = "0011"; a = 4; b = 2
# print(engine.findLexSmallestString(s,a,b), "0011")


# s = "74"; a=5; b=1
# print(engine.findLexSmallestString(s,a,b), "24")

s = "1830393069345171789354915923"; a=1; b=23
print(len(s))
print(engine.findLexSmallestString(s,a,b), "\n0000722832088524769686998638")

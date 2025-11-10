from functools import lru_cache

#non analytical
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n < 2:
            return n
        
        num = bin(n)[2:][::-1]
        
        @lru_cache(maxsize=None)
        def get_1_to_pos_clean(pos:int) -> int:
            if pos<0:
                return 0
            if pos == 0 :
                return 1
            return get_1_to_pos_clean(pos-1) +1 +if_1_on_pos_clean(pos-1)

        @lru_cache(maxsize=None)
        def if_1_on_pos_clean(pos:int) -> int:
            if pos == 0:
                return 1
            ops = get_1_to_pos_clean(pos-1)
            ops += 1
            ops += if_1_on_pos_clean(pos-1)
            return ops

        @lru_cache(maxsize=None)
        def clean_to(pos:int) -> int:
            if pos < 0:
                return 0
            if pos == 0:
                if num[0] == '1':
                    return 1
                else:
                    return 0

            if num[pos] == '0':
                return clean_to(pos-1)
            else:
                return fill_to(pos-1) + if_1_on_pos_clean(pos-1) +1

        @lru_cache(maxsize=None)
        def fill_to(pos:int) -> int:
            if pos < 0:
                return 0
            if pos == 0:
                if num[0] == '1':
                    return 0
                else:
                    return 1
            
            if num[pos] == '1':
                return clean_to(pos-1)
            else:
                return fill_to(pos-1) + if_1_on_pos_clean(pos-1) +1

        pos = len(num) -1
        if num[pos-1] == '1':
            ops = clean_to(pos-2)
            print(ops)
            ops += 1
            ops += if_1_on_pos_clean(pos-1)
        else:
            ops = fill_to(pos -1)
            ops += 1
            ops += if_1_on_pos_clean(pos -1)

        return ops
    


engine = Solution()

print(engine.minimumOneBitOperations(3), 2)
print(engine.minimumOneBitOperations(6), 4)
print(engine.minimumOneBitOperations(9), 14)

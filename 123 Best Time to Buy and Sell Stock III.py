from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0   
        
        ranges = []
        cur_min = prices[0]
        cur_max = cur_min
        for x in prices[1:]:
            if x <= cur_max:
                if cur_min< cur_max:
                    ranges.append((cur_min, cur_max))
                cur_min = x
            cur_max = x
        if cur_min< cur_max:
            ranges.append((cur_min, cur_max))

        def get_profit(ranges):
            cur_min, cur_max = ranges[0]
            profit = ((cur_max - cur_min, cur_min, cur_max))
            for low, high in ranges[1:]:
                if low <= cur_min and high>=cur_max:
                    cur_min = low
                    cur_max = high
                elif low > cur_min and high>=cur_max:
                    cur_max = high
                elif low > cur_min:
                    continue
                else:
                    if profit[0] < cur_max - cur_min:
                        profit = (cur_max - cur_min, cur_min, cur_max)
                    cur_min = low
                    cur_max = high

            if profit[0] < cur_max - cur_min:
                profit = (cur_max - cur_min, cur_min, cur_max)
            return profit

        if not ranges:
            return 0
        
        cur_max = get_profit(ranges)[0]
        if len(ranges) ==1:
            return cur_max

        left_profit = get_profit(ranges[:1])
        right_profit = get_profit(ranges[1:])
        cur_max = left_profit[0] + right_profit[0]

        right_changed = False
        for x in range(1,len(ranges)-1):
            range_min, range_max = ranges[x]
            if not right_changed:
                right_changed = right_profit[1] == range_min or right_profit[2] == range_max

            if left_profit[1] > range_min or left_profit[2] < range_max: 
                left_profit = get_profit(ranges[:x+1])
                if right_changed:
                    right_profit = get_profit(ranges[x+1:])
                    right_changed = False
              
                #max only changes when left changes, right can only go down
                cur_max = max(cur_max, left_profit[0] + right_profit[0]) 

        return cur_max
   
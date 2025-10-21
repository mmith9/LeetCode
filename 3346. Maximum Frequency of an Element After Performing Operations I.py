from collections import Counter, defaultdict
from typing import List

#ugly af
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        lens = len(nums)
        if lens <=1:
            return 1
        if numOperations == 0:
            return max(Counter(nums).values())

        nums.sort()
#        print(nums)

        max_x = len(nums)
        left = 0; right = -1; best_freq = 0
        rep_left = 0; rep_right = -1; cur_reps = 0; cur_repper = 0
        occus = defaultdict(int)
        freqs = [0]

#        print('#########')
#        print('count', lens)
#        print(nums, k, numOperations)
        while left + best_freq < max_x:
            right +=1; 

            while rep_right<right and nums[rep_right+1] <= nums[left] +k:
                rep_right+=1
                added = nums[rep_right]
                if added >= nums[right] -k:
                    occus[added] +=1
                    if occus[added] >= cur_reps:
                        cur_repper = added
                        cur_reps = occus[added]


            need_new_repper = False
            while nums[rep_left] < nums[right] -k:
                discarded = nums[rep_left]
                if discarded in occus:                    
                    del occus[discarded]
                rep_left += 1
                if discarded == cur_repper:
                    need_new_repper = True
#                print(f'discard {cur_repper=} {discarded=}')

            if need_new_repper:
                if not occus:
                    cur_reps = 0; cur_repper =0
                else:
                    cur_reps, cur_repper = max((value,-key) for key,value in occus.items())
                    cur_repper = -cur_repper

            while (nums[left] +k < nums[right] -k) or \
                (nums[left]+k < cur_repper and right - left >= numOperations) or \
                (right - left - cur_reps >= numOperations):
                
                left +=1

                while rep_right<right and nums[rep_right+1] <= nums[left] +k:
                    rep_right+=1
                    added = nums[rep_right]
                    if added >= nums[right] -k:
                        occus[added] +=1
                        if occus[added] >= cur_reps:
                            cur_repper = added
                            cur_reps = occus[added]

                need_new_repper = False
                while nums[rep_left] < nums[right] -k:
                    discarded = nums[rep_left]
                    if discarded in occus:                    
                        del occus[discarded]
                    rep_left += 1

                    if discarded == cur_repper:
                        need_new_repper = True
                
                if need_new_repper:
                    if not occus:
                        cur_reps = 0; cur_repper =0
                    else:
                        cur_reps, cur_repper = max((value,-key) for key,value in occus.items())
                        cur_repper = -cur_repper
                

            freq1 = right - left + 1
            best_freq = max(best_freq, freq1)
            # if right % 123 == 0:
#            print(f'{left=} {rep_left=} {rep_right=} {right=} {best_freq=} {cur_repper=} {cur_reps=} {len(occus)=} {occus}')


        return best_freq
 
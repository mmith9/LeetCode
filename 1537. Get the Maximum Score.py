from typing import List

#simple iteration over set intersection
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0; idx1 = 0; idx2 = 0
        switches = list(set(nums1).intersection(nums2))
        switches.sort()
        for sw in switches:
            nidx1 = nums1.index(sw, idx1)
            nidx2 = nums2.index(sw, idx2)
            res += max(sum(nums1[idx1:nidx1]), sum(nums2[idx2:nidx2]))
            idx1, idx2 = nidx1, nidx2
        res += max(sum(nums1[idx1:]), sum(nums2[idx2:]))
        return res %(10**9+7)
 

#dp solution. only beats 33%
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        switches = set(nums1).intersection(set(nums2))
        sums = [{},{}]
        switches_o = [0]
        for lane, nums in enumerate([nums1, nums2]):
            start = 0; summ = 0
            for num in nums:
                if num not in switches:
                    summ += num
                else:
                    sums[lane][start] = summ
                    summ = num
                    start = num
                    if lane:
                        switches_o.append(num)
            sums[lane][start] = summ

        dp = [[0],[0]]
        for idx, switch in enumerate(switches_o):
            for cur_lane, sumz in enumerate(sums):
                oth_lane = 1 - cur_lane

                s1 = dp[cur_lane][idx] + sums[cur_lane][switch]
                s2 = dp[cur_lane][idx] + sums[oth_lane][switch]
                if s2>s1:
                    dp[cur_lane].append(s2)
                else:
                    dp[cur_lane].append(s1)

        res = max(dp[0][-1], dp[1][-1])

        return res %(10**9+7)
    

engine = Solution()

nums1 = [2,4,5,8,10]; nums2 = [4,6,8,9]
print(engine.maxSum(nums1,nums2), 30)

nums1 = [1,3,5,7,9]; nums2 = [3,5,100]
print(engine.maxSum(nums1,nums2), 109)

nums1 = [1,2,3,4,5]; nums2 = [6,7,8,9,10]
print(engine.maxSum(nums1,nums2), 40)

from typing import List


#DP 1d, linescan
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        l1 = len(nums1)-1; l2 = len(nums2)-1
        line = [nums1[l1]*nums2[l2]]

        n2 = nums2[l2]
        for a in nums1[:-1][::-1]:
            line.append(max(line[-1], a*n2))

        for y in range(l2-1,-1,-1):
            newline = []
            n2 = nums2[y]
            newline.append(max(line[0], nums1[l1]*n2))
            lastb = line[0]
            for a, b in zip(nums1[:-1][::-1], line[1:]):
                newline.append(max(b, newline[-1], lastb + a*n2, a*n2))
                lastb = b
            line = newline

        return line[-1]


#wicked 2 dimension - reversed and with appends
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        l1 = len(nums1); l2 = len(nums2)
        dp = [[] for _ in range(l2)]
        l1-=1;l2-=1

        dp[l2].append(nums1[l1]*nums2[l2])

        dp_row = dp[l2]; n2 = nums2[l2]
        for a in nums1[:-1][::-1]:
            dp_row.append(max(dp_row[-1], a*n2))

        for y in range(l2-1,-1,-1):
            dp_row = dp[y]; n2 = nums2[y]
            dp_row.append(max(dp[y+1][0], nums1[l1]*n2))
            lastb = dp[y+1][0]
            for a, b in zip(nums1[:-1][::-1], dp[y+1][1:]):
                dp_row.append(max(b, dp_row[-1], lastb + a*n2, a*n2))
                lastb = b

        return dp[0][l1]


#dp 100ms classic 2dimension
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        l1 = len(nums1); l2 = len(nums2)
        dp = [[0]*l1 for _ in range(l2)]
        l1-=1;l2-=1

        dp[l2][l1] = nums1[l1]*nums2[l2]

        dp_row = dp[l2]; n2 = nums2[l2]
        for x in range(l1-1,-1,-1):
            dp_row[x] = max(dp_row[x+1], nums1[x]*n2)

        for y in range(l2-1,-1,-1):
            dp_row = dp[y]; n2 = nums2[y]
            dp_row[l1] = max(dp[y+1][l1], nums1[l1]*n2)
            for x in range(l1-1,-1,-1):
                dp_row[x] = max(dp[y+1][x], dp_row[x+1], dp[y+1][x+1] + nums1[x]*n2, nums1[x]*n2)

        return dp[0][0]


engine = Solution()


# nums1 = [2,1,-2,5]; nums2 = [3,0,-6]
# print(engine.maxDotProduct(nums1, nums2), 18)

# nums1 = [3,-2]; nums2 = [2,-6,7]
# print(engine.maxDotProduct(nums1, nums2), 21)


# nums1 = [-1,-1]; nums2 = [1,1]
# print(engine.maxDotProduct(nums1, nums2), -1)

nums1 = [-5,-1,-2]; nums2 = [3,3,5,5]
print(engine.maxDotProduct(nums1, nums2), -3)


nums1 = [5,-4,-3]
nums2 = [-4,-3,0,-4,2]
print(engine.maxDotProduct(nums1, nums2), 28)
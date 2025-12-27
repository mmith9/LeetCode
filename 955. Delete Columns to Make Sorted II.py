from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        
        res = 0; lens = len(strs); to_check = range(0, lens); ok_cols = []
        for col in range(len(strs[0])):
            last = ' '
            new_check = []
            is_break = False
            for x in to_check:
                c = strs[x][col]
                if c < last:
                    for i in ok_cols:
                        if strs[x-1][i] < strs[x][i]:
                            break
                    else:
                        is_break = True
                        res +=1

                if is_break:
                    is_break = False
                    break

                if c == last:
                    for i in ok_cols:
                        if strs[x-1][i] < strs[x][i]:
                            break
                    else:
                        if not new_check or new_check[-1] != x-1:
                            new_check.append(x-1)
                        new_check.append(x)
                last = c
            else:
                if not new_check:
                    return res
                to_check = new_check
                ok_cols.append(col)
#            print(res, to_check, ok_cols)

        return res



engine = Solution()

strs = ["ca","bb","ac"]
print(engine.minDeletionSize(strs), 1)

strs = ["xc","yb","za"]
print(engine.minDeletionSize(strs), 0)

strs = ["zyx","wvu","tsr"]
print(engine.minDeletionSize(strs), 3)

strs = ["xga","xfb","yfa"]
print(engine.minDeletionSize(strs), 1)

strs = ["zyx","wvu","tsr"]
print(engine.minDeletionSize(strs), 3)

strs = ["abx","agz","bgc","bfc"]
print(engine.minDeletionSize(strs), 1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        valids = []
        max_len = 0
        for pos, char in enumerate(s):
            if char == '(':
                stack.append(pos)
            else:
                if stack:
                    last_pos = stack.pop()
                    while valids and valids[-1][0] > last_pos and valids[-1][1] < pos:
                        valids.pop()
                    if valids and valids[-1][1] +1 == last_pos:
                        last_pos, _ = valids.pop()
                    valids.append((last_pos, pos))

        for a,b in valids:
            max_len = max(max_len, b-a+1)
        return max_len
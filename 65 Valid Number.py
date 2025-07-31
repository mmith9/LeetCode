class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        nums = [str(x) for x in range(10)]
        if s[0] not in (nums + ['+', '-', '.']):
            return False
        s=s.lower()
        if s[-1] in ['-','+','e']:
            return False

        got_dot = False
        got_exp = False
        last_was_exp = False
        last_was_dot = False
        got_num = False
        got_exp_num = False
        is_first_char = True

        for char in s:
            if is_first_char:
                is_first_char = False
                if char in ['-', '+']:
                    continue
                
            if last_was_exp:
                last_was_exp = False
                if char in ['-', '+']:
                    continue

            if char in nums:
                if got_exp:
                    got_exp_num = True
                else:
                    got_num = True
                continue

            if char == '.' and not got_dot and not got_exp:
                got_dot = True
                continue

            if char == 'e' and not got_exp:
                got_exp = True
                got_dot = True
                last_was_exp = True
                continue
            return False
        
        if not got_num:
            return False
        if got_exp and not got_exp_num:
            return False
        
        return True
class Solution(object):
    def myAtoi(self,s):
        n = len(s)
        i = 0
        sign = 1
        num = 0

        # 1. Leading Spaces 
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read Digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign

        # 4. Clamp to 32-bit signed integer range 
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
class Solution:
    def myAtoi(self, s: str) -> int:
        #2:44

        i = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i] == ' ':
            i+=1

        sign = 1
        if i < len(s) and s[i] == '-':
            sign = -1
            i+=1
        elif i < len(s) and s[i] == '+':
            i+=1 
        
        while i < len(s) and s[i] == '0':
            i+=1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num *= 10
            num += int(s[i])
            i+=1
            if num > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN

        return num * sign

        
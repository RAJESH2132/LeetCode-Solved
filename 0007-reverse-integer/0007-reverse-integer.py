class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x*(-1) if sign < 0 else x
        low = -2**31
        high = 2**31-1
        revNum = 0
        while x:
            digit = x % 10
            revNum = revNum * 10 + digit
            x = x // 10
        if revNum < low or revNum > high :
            return 0
        return revNum*sign
        
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        low, high = -2**31, 2**31 - 1
        revNum = 0
        
        while x:
            digit = x % 10
            if revNum > (high - digit) // 10:
                return 0  # Prevent overflow
            revNum = revNum * 10 + digit
            x //= 10
            
        return revNum * sign
        
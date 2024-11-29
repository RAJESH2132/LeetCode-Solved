class Solution:
    def reverse(self, n: int) -> int:
        INT_MAX = 2**31 - 1  # Maximum 32-bit signed integer
        INT_MIN = -2**31     # Minimum 32-bit signed integer

        # Determine the sign and work with the absolute value of n
        sign = -1 if n < 0 else 1
        n = abs(n)

        # Reverse the number
        reversed_num = 0
        while n > 0:
            digit = n % 10
            reversed_num = reversed_num * 10 + digit
            n //= 10

        # Check for overflow
        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0
        
        return sign * reversed_num


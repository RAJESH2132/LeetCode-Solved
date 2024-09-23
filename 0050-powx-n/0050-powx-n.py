class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        n = abs(n)  # Make n positive
        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= x
                n -= 1
            x *= x  # Square the base
            n //= 2  # Halve the exponent
        return 1 / result if is_negative else result
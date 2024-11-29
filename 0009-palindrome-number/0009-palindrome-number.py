class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Reverse the number
        temp = 0
        original = x
        while x > 0:
            temp = temp * 10 + (x % 10)
            x //= 10

        # Check if the reversed number matches the original
        return temp == original

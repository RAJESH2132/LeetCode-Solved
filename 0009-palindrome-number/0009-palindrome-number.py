class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it's not a palindrome
        if x < 0:
            return False
        
        # Convert the number to a string
        str_x = str(x)
        
        # Check if the string is the same as its reverse
        return str_x == str_x[::-1]
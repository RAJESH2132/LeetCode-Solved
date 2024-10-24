class Solution:
    def isPalindrome(self, n: int) -> bool:
        # -----------------------Solution1---------------------------------
        # If the number is negative, it's not a palindrome
        if n < 0:
            return False
        
        # Convert the number to a string
        str_x = str(n)
        
        # Check if the string is the same as its reverse
        return str_x == str_x[::-1]

        # --------------------------Solution2----------------------------------
        # original = n
        # revNum = 0
        # while n > 0:
        #     digit = n % 10
        #     revNum = revNum * 10 + digit
        #     n = n // 10
        # if original != revNum:
        #     return False
        # return True
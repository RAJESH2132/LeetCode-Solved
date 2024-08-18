class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkPalindrome(i: int, s: str) -> bool:
            # Base condition: Check if we have reached the middle of the string
            if i >= len(s) // 2:
                return True
            
            # Check if the characters at the current indices are the same
            if s[i] != s[len(s) - i - 1]:
                return False
            
            # Recursive call to check the next pair of characters
            return checkPalindrome(i + 1, s)
        
        # Normalize the string: remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Start the recursive palindrome check
        return checkPalindrome(0, s)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around the center and find the longest palindrome
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring found
            return s[left + 1:right]
        
        # Base case: if the string is empty or has only one character
        if not s or len(s) == 1:
            return s
        
        longest_palindrome = ""
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            palindrome1 = expandAroundCenter(i, i)
            # Even-length palindromes (two characters center)
            palindrome2 = expandAroundCenter(i, i + 1)
            
            # Update the longest palindrome found
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
        
        return longest_palindrome

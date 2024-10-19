class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        def checkPalindrome(s,i,j):
            if i >= j :
                return True
            if s[i] != s[j]:
                return False
            return checkPalindrome(s,i+1,j-1)
        return checkPalindrome(s,0,len(s)-1)
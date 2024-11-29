class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 and x == 0:
            return False
        temp = 0
        original = x
        while x > 0:
            temp = temp*10 + (x%10)
            x //= 10
        if temp == original:
            return True
        return False
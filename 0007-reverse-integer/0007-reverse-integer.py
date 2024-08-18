class Solution:
    def reverse(self, x: int) -> int:
        max_int=2**31-1
        min_int=-2**31
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        num=0
        while(x!=0):
            num = (num*10)+(x%10)
            x//=10
        if num>=max_int or num<=min_int:
            return 0
        return num * -1 if is_negative else num
        
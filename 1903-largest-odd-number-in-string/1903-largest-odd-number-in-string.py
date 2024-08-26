class Solution:
    def largestOddNumber(self, num: str) -> str:
        group = []
        maxx = -1
        if int(num)%2!=0:
            return num
        else:
            for i in num:
                x = int(i)
                if x%2!=0:
                    if x > int(maxx):
                        maxx = i
            if maxx == -1:
                return ""
            return maxx
        
        return ""

            



        
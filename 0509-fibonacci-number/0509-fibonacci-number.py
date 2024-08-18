class Solution:
    def fib(self, n: int) -> int:
        demo=[0,1]
        if n <= 1:
            return n
        for i in range(2, n+1):
            demo.append(demo[i-1]+demo[i-2])
        return demo[-1]
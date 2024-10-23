class Solution(object):
    def fn(self, n, dp):
        if n <= 1: 
            return n
        if dp[n] != -1: 
            return dp[n]
        dp[n] = self.fn(n-1, dp) + self.fn(n-2, dp)
        return dp[n]
    def fib(self, n):
        dp = [-1] * (n + 1)
        return self.fn(n, dp)
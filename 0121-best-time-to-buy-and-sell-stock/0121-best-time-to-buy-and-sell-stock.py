class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minElement = float("inf")
        for i in range(len(prices)):
            minElement = min(minElement, prices[i])
            maxProfit = max(maxProfit, prices[i]-minElement)
        return maxProfit
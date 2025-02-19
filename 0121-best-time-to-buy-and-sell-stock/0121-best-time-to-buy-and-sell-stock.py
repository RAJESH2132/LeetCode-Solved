class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float('inf')

        for price in prices:
            minPrice = min(minPrice, price)  # Update minPrice
            maxPro = max(maxPro, price - minPrice)  # Calculate max profit

        return maxPro

        
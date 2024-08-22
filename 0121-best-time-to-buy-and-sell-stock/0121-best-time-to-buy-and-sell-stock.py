class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        priceMin = float("inf")
        priceMax = 0
        for num in prices:
            priceMin = min(priceMin,num)
            priceMax = max(priceMax,num-priceMin)
        return priceMax

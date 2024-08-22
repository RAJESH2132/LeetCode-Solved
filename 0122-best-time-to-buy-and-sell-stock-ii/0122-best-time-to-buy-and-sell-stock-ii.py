class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0  # This variable will store the maximum profit.
        start = prices[0]  # Start with the first day's price.
        
        for num in prices:
            if start < num:  # If the current price is higher than the starting price (previous day price),
                maxPrice += num - start  # add the difference to maxPrice.
            start = num  # Update start to the current day's price for the next iteration.
        
        return maxPrice  # Return the total accumulated profit.

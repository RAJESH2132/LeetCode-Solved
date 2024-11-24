class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        max_sum = float('-inf')  # Initialize max sum to the smallest possible value
        current_sum = 0  # Initialize current sum as 0

        for num in arr:
            current_sum += num  # Add current element to current_sum
            current_sum = max(current_sum, num)  # Choose the larger: extend or start fresh
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed

        return max_sum
        
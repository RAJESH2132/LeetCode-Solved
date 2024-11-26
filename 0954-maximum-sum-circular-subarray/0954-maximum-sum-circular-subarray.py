class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        def kadane(arr):
            max_sum = current_sum = arr[0]
            for num in arr[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
    
        # Calculate the total sum of the array and the minimum subarray sum
        total_sum = sum(arr)
        max_subarray = kadane(arr)  # Maximum subarray sum in normal (non-circular) case

        # Calculate the minimum subarray sum by inverting the array
        inverted_arr = [-x for x in arr]
        min_subarray = kadane(inverted_arr)

        # The maximum circular subarray sum will be the maximum of the following:
        # 1. The normal max subarray sum
        # 2. Total sum of array - the minimum subarray sum (circular part)
        if total_sum == -min_subarray:  # This case occurs when all elements are negative
            return max_subarray

        return max(max_subarray, total_sum + min_subarray)
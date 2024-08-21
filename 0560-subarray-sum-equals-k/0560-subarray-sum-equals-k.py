class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0  # This will store the total number of subarrays whose sum equals k.
        prefix_sum = 0  # This variable keeps track of the cumulative sum of elements as we iterate through the list.
        dictionary = {0: 1}  # A dictionary to store the frequency of prefix sums. We initialize it with 0:1 to handle the case where a subarray itself equals k.

        for num in nums:
            prefix_sum += num  # Update the cumulative sum with the current element.

            # Check if there's a prefix sum that, when subtracted from the current prefix sum, equals k.
            if prefix_sum - k in dictionary:
                result += dictionary[prefix_sum - k]  # If found, increment the result by the frequency of that prefix sum.

            # Update the dictionary to include the current prefix sum.
            if prefix_sum not in dictionary:
                dictionary[prefix_sum] = 1  # If the prefix sum is not in the dictionary, add it with a frequency of 1.
            else:
                dictionary[prefix_sum] += 1  # If the prefix sum is already in the dictionary, increment its frequency.

        return result  # Return the total count of subarrays whose sum equals k.

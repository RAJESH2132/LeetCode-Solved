class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Finds the maximum number of consecutive 1s in the binary array.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0       # To count the current streak of consecutive 1s
        max_count = 0   # To track the maximum streak of consecutive 1s

        for num in nums:
            if num == 1:
                count += 1    # Increment the streak count
                max_count = max(max_count, count)  # Update maximum if needed
            else:
                count = 0     # Reset count if the streak breaks

        return max_count

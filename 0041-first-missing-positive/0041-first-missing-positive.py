class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        # Step 1: Filter only positive numbers and create a set
        positive_numbers = set(num for num in arr if num > 0)

        # Step 2: Check for the smallest missing positive starting from 1
        smallest = 1
        while smallest in positive_numbers:
            smallest += 1

        return smallest
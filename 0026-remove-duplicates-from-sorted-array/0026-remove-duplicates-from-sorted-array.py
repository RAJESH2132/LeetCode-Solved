class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # If the list is empty, no duplicates to remove
            return 0
        
        # Initialize a pointer to track the position of the last unique element
        unique_index = 0
        
        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[unique_index]:  # If the current element is different
                unique_index += 1  # Move the unique pointer
                nums[unique_index] = nums[i]  # Update the position with the unique element
        
        return unique_index + 1  # The length of the array without duplicates is unique_index + 1

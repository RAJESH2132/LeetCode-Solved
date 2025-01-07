class Solution:
    
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Step 1: Find where the sorted order breaks
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                break
        else:
            return True  # If no break occurs, the array is already sorted
        
        # Step 2: Check if the remaining part is sorted
        is_remaining_sorted = True
        for j in range(i, n - 1):
            if nums[j] > nums[j + 1]:
                is_remaining_sorted = False
                break
        
        # Step 3: Check if the last element is <= first element
        is_last_less_equal_first = nums[n - 1] <= nums[0]
        
        # Step 4: Return final result
        return is_remaining_sorted and is_last_less_equal_first

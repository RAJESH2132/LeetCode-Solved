class Solution:
    def rotation(self, nums: List[int], start: int, end: int) -> None:
        # This function reverses the elements in the list 'nums' from index 'start' to 'end'
        while start <= end:
            # Swap the elements at positions 'start' and 'end'
            nums[start], nums[end] = nums[end], nums[start]
            # Move 'start' forward and 'end' backward to continue the reversal
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)  # Get the length of the list
        k = k % n  # In case 'k' is greater than 'n', reduce 'k' to a manageable size
        
        # Step 1: Reverse the first part of the list from index 0 to n-k-1
        self.rotation(nums, 0, n - k - 1)
        
        # Step 2: Reverse the second part of the list from index n-k to n-1
        self.rotation(nums, n - k, n - 1)
        
        # Step 3: Reverse the entire list to complete the right rotation by 'k' positions
        self.rotation(nums, 0, n - 1)

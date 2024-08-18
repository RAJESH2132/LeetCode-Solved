class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        
        # Move non-zero elements to the front of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # Fill the remaining positions with zeroes
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

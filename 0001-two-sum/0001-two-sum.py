class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Dictionary to store seen numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # If not, add the current number to the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list or handle it as needed
        return []
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function to find the first occurrence of the target
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first_occurrence = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    high = mid - 1  # Keep searching to the left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return first_occurrence
        
        # Function to find the last occurrence of the target
        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last_occurrence = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    low = mid + 1  # Keep searching to the right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return last_occurrence
        
        # Call the helper functions to get the first and last occurrence
        first_occurrence = findFirst(nums, target)
        last_occurrence = findLast(nums, target)
        
        return [first_occurrence, last_occurrence]

        
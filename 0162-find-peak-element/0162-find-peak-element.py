class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = len(nums)

        # Edge cases:
        if s == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[s - 1] > nums[s - 2]:
            return s - 1

        # Binary search for O(log n) solution
        l, h = 1, s - 2  # Start from 1 and end at s-2 to avoid boundary issues
        while l <= h:
            mid = l + (h - l) // 2

            # Check if the middle element is a peak element
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # If the element to the right of mid is greater, move the left pointer
            elif nums[mid + 1] > nums[mid]:
                l = mid + 1
            # Otherwise, move the right pointer
            else:
                h = mid - 1

        return -1  # This return is just a safety net; logically, the code should never reach here.
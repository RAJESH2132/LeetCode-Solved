class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        if n == 1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[n-1] > nums[n-2]:
            return n-1
        
        while low <= high:
            mid = low + (high-low)//2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[mid-1]:
                low = mid+1
            else:
                high = mid-1
        return -1
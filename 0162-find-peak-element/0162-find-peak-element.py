class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        while low <= high:
            mid = ((high-low)//2) + low
            # Peak element is present in right side
            if nums[mid] < nums[mid+1]:
                low = mid+1
            # Peak element is present in left side
            elif nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                return mid

        
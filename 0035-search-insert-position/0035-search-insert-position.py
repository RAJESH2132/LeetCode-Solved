class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        ans = n

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]>=target:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
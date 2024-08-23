class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        if k == -1:
            nums.reverse()
            return
        l = len(nums) - 1
        while nums[l] <= nums[k]:
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        left, right = k + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
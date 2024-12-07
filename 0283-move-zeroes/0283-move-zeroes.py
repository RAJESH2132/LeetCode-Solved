class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Optimized version with single pass.
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != 0:
                # Swap current element with the element at the `index` position
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

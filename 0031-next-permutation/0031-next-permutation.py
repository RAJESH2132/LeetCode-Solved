class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n-1
        i = idx - 1
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                break
        if i > -1:
            for j in range(n-1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        i += 1
        while i < idx:
            nums[idx], nums[i] = nums[i], nums[idx]
            i += 1
            idx -= 1
            
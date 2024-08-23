class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return

        # find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # if i is not the first element, swap nums[i] with the next larger element
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the elements after the swapped element
        nums[i + 1:] = nums[i + 1:][::-1]
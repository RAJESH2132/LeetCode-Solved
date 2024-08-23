class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Step 1: Find the break point:
        ind = -1 # break point
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        
        # If break point does not exist:
        # Reverse the Whole Array
        if ind == -1:
            nums.reverse()
            return
        
        # Step 2: Find the next greater element
        #   and swap it with arr[ind]:
        for i in range(n-1,-1,-1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        
        # Step 3: reverse the right half:
        nums[ind+1:] = reversed(nums[ind+1:])
        
        
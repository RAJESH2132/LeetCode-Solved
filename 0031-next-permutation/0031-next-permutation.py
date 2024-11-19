class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            self.rotated(nums, 0, n)
            return
            
        for i in range(n-1,-1,-1):
            if nums[i]>nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        self.rotated(nums,index+1,n)
    
    def rotated(self,arr,start,end):
        left = start
        right = end-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # return arr

       
        
        
class Solution:
    def getMax(self,arr,l,r,maxx):
        return maxx.append(max(arr[l:r+1]))


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        maxx = []

        while right < k-1:
            right += 1
        
        while right < len(nums):
            self.getMax(nums,left,right,maxx)
            left += 1
            right += 1
        return maxx
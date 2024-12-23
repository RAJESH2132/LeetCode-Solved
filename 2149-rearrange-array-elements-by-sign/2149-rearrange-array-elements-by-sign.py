class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIndex = 0
        negIndex = 1
        n = len(nums)
        result = [0]*n
        for i in range(n):
            if nums[i] > 0:
                result[posIndex] = nums[i]
                posIndex += 2
            else:
                result[negIndex] = nums[i]
                negIndex += 2
        return result 

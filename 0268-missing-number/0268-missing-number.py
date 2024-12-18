class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nSum = n*(n+1)//2

        eleSum = 0
        for i in nums:
            eleSum += i
        
        return nSum-eleSum
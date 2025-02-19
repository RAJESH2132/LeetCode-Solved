class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float("-inf")
        total = 0
        for i in range(n):
            total += nums[i]
            maxSum = max(maxSum,total)
            if total < 0:
                total = 0
        return maxSum
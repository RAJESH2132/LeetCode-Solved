class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = float("-inf")
        Sum = 0
        for i in range(n):
            Sum += nums[i]
            if Sum > maxx:
                maxx = max(Sum,maxx)
            if Sum <= 0:
                Sum = 0
        return maxx
        
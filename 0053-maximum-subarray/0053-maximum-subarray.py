class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float("-inf")
        Sum = 0
        for num in nums:
            Sum += num
            if Sum > maxx:
                maxx = max(Sum,maxx)
            if Sum <= 0:
                Sum = 0
        return maxx
        
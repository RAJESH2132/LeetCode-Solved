class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n*(n+1))//2
        S2 = 0
        for i in range(n):
            S2+=nums[i]
        result = sum - S2
        return result
        
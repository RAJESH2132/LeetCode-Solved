import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n > threshold:
            return -1
        low = 1
        high = max(nums)
        # ans = 0
        while low <= high:
            mid = (low+ high)//2

            ans = 0
            for i in range(n):
                ans += math.ceil(nums[i]/mid)
            if ans <= threshold:
                high = mid-1
            else:
                low = mid +1
        return low


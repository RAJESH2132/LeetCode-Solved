from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = defaultdict(int)
        preSum = 0
        count = 0
        n = len(nums)
        if n ==1 and nums[0] == k:
            return 1
        for num in nums:
            preSum += num
            remove = preSum - num
            count += dictt[remove]
            dictt[preSum]+=1
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = {0:1}
        preSum = 0
        count = 0
        n = len(nums)
        dictt[0] = 1
        
        for num in nums:
            preSum += num
            remove = preSum - k
            if remove in dictt:
                count += dictt[remove]
            if preSum in dictt:
                dictt[preSum] += 1
            else:
                dictt[preSum] = 1
            
        return count
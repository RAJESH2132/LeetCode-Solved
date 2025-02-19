from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        maxVals = []
        for i in range(len(nums)):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if i >= k-1:
                maxVals.append(nums[dq[0]])
        return maxVals
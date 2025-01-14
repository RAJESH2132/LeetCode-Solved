class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = -1
        n = len(nums)
        for i in range(n):
            if count == 0 :
                count = 1
                element = nums[i]
            elif nums[i] == element:
                count += 1
            else:
                count -= 1
        return element 
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_array = sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i] == sorted_array:
                return True
        return False
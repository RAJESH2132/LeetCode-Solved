class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1 << n  # 2^n
        result = []
        
        # Iterate through all numbers from 0 to 2^n - 1
        for mask in range(total_subsets):
            current_subset = []
            for i in range(n):
                # Check if the ith bit in the mask is set (1)
                if mask & (1 << i):
                    current_subset.append(nums[i])
            result.append(current_subset)
        
        return result
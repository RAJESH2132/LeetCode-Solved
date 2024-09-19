class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        n = len(nums)
        
        # XOR all elements to get xor_all (which will be the XOR of the two odd occurring numbers)
        for num in nums:
            xor_all ^= num
        
        # Find the rightmost set bit in xor_all (which is different in the two odd occurring numbers)
        rightmost_set_bit = xor_all & -xor_all
        
        # Divide numbers into two groups based on the rightmost set bit
        x = 0
        y = 0
        
        for num in nums:
            if num & rightmost_set_bit:
                x ^= num  # Numbers with the set bit
            else:
                y ^= num  # Numbers without the set bit
        
        # Return the two odd occurring numbers in decreasing order
        return sorted([x, y], reverse=True)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Xor = 0
        for ele in nums:
            Xor ^= ele
        return Xor
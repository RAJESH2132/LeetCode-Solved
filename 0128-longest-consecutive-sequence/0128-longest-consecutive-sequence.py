class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        st = set()
        for i in range(n):
            st.add(nums[i])
        
        for it in st:
            if it-1 not in st:
                count = 1
                while it+1 in st:
                    count += 1
                    it += 1
                longest = max(longest, count)
        return longest
                


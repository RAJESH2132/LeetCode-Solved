class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxDepth = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1

            maxDepth = max(maxDepth, count)

        return maxDepth
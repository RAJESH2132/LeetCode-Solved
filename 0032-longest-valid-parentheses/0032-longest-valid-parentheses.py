class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        n = len(s)
        
        # Check all possible substrings
        for i in range(n):
            open_count = 0
            close_count = 0
            for j in range(i, n):
                if s[j] == '(':
                    open_count += 1
                else:
                    close_count += 1
                
                # If at any point close_count exceeds open_count, the substring is invalid
                if close_count > open_count:
                    break
                
                # If open_count == close_count, it's a valid parentheses substring
                if open_count == close_count:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
    
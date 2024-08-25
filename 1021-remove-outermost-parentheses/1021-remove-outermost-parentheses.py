class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0

        for char in s:
            if char == ')':
                count -= 1
            if count != 0:
                ans.append(char)
            if char == '(':
                count += 1

        return ''.join(ans)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''

        stack = []

        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                index_pos = stack.pop()
                if not stack:
                    result+=s[index_pos+1:i]
        return result



        
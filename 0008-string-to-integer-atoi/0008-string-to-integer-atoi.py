########################################### 1)Recursive Approach #############################################
'''class Solution:
    def myAtoi(self, s: str) -> int:
        return self.atoiRecursive(s)

    def atoiRecursive(self,s: str, i: int = 0, sign: int = 1, ans: int = 0, sign_processed: bool = False) -> int:
        # Base case: If we've reached the end of the string, return the result
        if i >= len(s):
            return ans * sign

        # If we encounter leading whitespaces, continue with the recursion
        if not sign_processed and s[i] == " ":
            return self.atoiRecursive(s, i + 1, sign, ans, sign_processed)

        # Handle the sign if it appears at the current index and if sign not yet processed
        if not sign_processed and (s[i] == "-" or s[i] == "+"):
            new_sign = -1 if s[i] == "-" else 1
            return self.atoiRecursive(s, i + 1, new_sign, ans, True)

        # If the current character is a digit, accumulate it to the result
        if s[i].isdigit():
            new_ans = ans * 10 + int(s[i])

            # Handle overflow conditions
            if new_ans * sign < -2**31:
                return -2**31
            if new_ans * sign > 2**31 - 1:
                return 2**31 - 1

            return self.atoiRecursive(s, i + 1, sign, new_ans, True)

        # If any non-digit and non-whitespace character is encountered, stop and return the result
        return ans * sign
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        i = 0
        n = len(s)

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert the digits to an integer
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if ans * sign <= -2**31:
                return -2**31
            if ans * sign >= 2**31 - 1:
                return 2**31 - 1
            i += 1

        return ans * sign
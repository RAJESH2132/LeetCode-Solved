class Solution:
    def maxDepth(self, s: str) -> int:
        depth = []
        level = 0
        for c in s:
            if c == "(":
                level +=1
            elif c == ")":
                level -=1
            depth.append(level)
        return max(depth)
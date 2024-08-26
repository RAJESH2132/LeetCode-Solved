class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        # Start with the first string as the common prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        return prefix



            

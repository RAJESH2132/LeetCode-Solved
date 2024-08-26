class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = words[::-1]

        rev_string = ' '.join(rev_words)

        return rev_string
        
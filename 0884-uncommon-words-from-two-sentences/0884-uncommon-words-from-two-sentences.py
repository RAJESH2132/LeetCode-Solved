class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words and count occurrences in both sentences
        count = Counter(s1.split()) + Counter(s2.split())
        
        # Return words that appear exactly once
        return [word for word in count if count[word] == 1]
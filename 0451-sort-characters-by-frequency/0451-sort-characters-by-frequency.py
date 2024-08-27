class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        # Step 2: Sort the characters by how often they appear, in descending order
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
    
        # Step 3: Build the result string by repeating each character based on its frequency
        result = ''.join([char * count for char, count in sorted_chars])
    
        return result
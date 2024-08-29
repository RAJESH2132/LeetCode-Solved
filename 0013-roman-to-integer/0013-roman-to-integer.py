class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the Roman numeral string in reverse
        for char in reversed(s):
            value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            
            # Update previous value for the next iteration
            prev_value = value
        
        return total
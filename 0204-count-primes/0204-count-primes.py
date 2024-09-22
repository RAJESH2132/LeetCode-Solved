class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0  # There are no primes less than 2

        # Step 1: Create a boolean array "is_prime" and initialize all entries as True
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
        # Step 2: Mark non-primes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:  # If i is still marked as prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
    
        # Step 3: Count the number of primes
        return sum(is_prime)
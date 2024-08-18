class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        j = -1
        n = len(a)
        # Place the pointer j
        for i in range(n):
            if a[i] == 0:
                j = i
                break

        # No non-zero elements
        if j == -1:
            return a

        # Move the pointers i and j and swap accordingly
        for i in range(j + 1, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j += 1
                        



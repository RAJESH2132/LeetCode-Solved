class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # First pass: find all zeros
        out = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    out.append([i,j])
        
        # Extract rows and columns that should be zeroed
        cols = []
        rows = []
        for li in out:
            rows.append(li[0])
            cols.append(li[1])

        # Second pass: Set the appropriate rows and columns to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
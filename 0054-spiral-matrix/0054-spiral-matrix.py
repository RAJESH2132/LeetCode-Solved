class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m-1
        top = 0
        bottom = n-1
        ans = []

        while (top <= bottom and left <= right):

            # Right Direction (Left --> Right)
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            # Bottom Direction (right side top --> Bottom)
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            # left Direction (bottom right --> left)
            if (top <= bottom):
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Top Direction (left side Bottom --> Top)
            if (left <= right):
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
        



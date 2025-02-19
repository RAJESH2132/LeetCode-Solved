class Solution:
    def generateRow(self,row):
        ans = 1
        ansRow = [1]
        for col in range(1,row):
            ans *= (row-col)
            ans //= col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        triangle = []
        for i in range(1,n+1):
            triangle.append(self.generateRow(i))
        return triangle
        
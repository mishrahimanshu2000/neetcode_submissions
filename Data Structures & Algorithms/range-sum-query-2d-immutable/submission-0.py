class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        mat_sum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                mat_sum[i][j] = mat_sum[i-1][j] + mat_sum[i][j-1] - mat_sum[i-1][j-1] + matrix[i-1][j-1] 
            
        self.mat_sum = mat_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        temp = self.mat_sum[row2+1][col1] + self.mat_sum[row1][col2+1] - self.mat_sum[row1][col1]
        return self.mat_sum[row2+1][col2+1] - temp



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
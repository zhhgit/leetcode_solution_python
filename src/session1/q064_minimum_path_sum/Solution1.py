class Solution1:
    def minPathSum(self, grid):
        rowLen = len(grid)
        columnLen = len(grid[0])
        if columnLen == 0 or rowLen == 0:
            return 0
        if columnLen == 1 and rowLen == 1:
            return grid[0][0]
        matrix = [[0 for i in range(0,columnLen)] for j in range(0,rowLen)]
        for i in range(0,rowLen):
            for j in range(0,columnLen):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1] + grid[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] + grid[i][j]
                else:
                    matrix[i][j] = min(matrix[i][j - 1],matrix[i - 1][j]) + grid[i][j]
        return matrix[rowLen - 1][columnLen - 1]

s = Solution1()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(s.minPathSum(grid))


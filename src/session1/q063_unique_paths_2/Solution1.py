class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rowLen = len(obstacleGrid)
        columnLen = len(obstacleGrid[0])
        matrix = [[0 for i in range(columnLen)] for j in range(rowLen)]
        for i in range(0,rowLen):
            for j in range(0,columnLen):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = 1
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = matrix[i - 1][j]
                else:
                    if obstacleGrid[i][j] == 1:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[rowLen - 1][columnLen - 1]

matrix = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
s = Solution1()
print(s.uniquePathsWithObstacles(matrix))

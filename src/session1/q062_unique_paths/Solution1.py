class Solution1:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        matrix = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    matrix[i][j] = 0
                elif i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]

m = 1
n = 2
s = Solution1()
print(s.uniquePaths(m,n))

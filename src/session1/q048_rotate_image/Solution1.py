class Solution1:
    def rotate(self, matrix):
        matrixLen = len(matrix)
        roundTime = matrixLen // 2
        for i in range(0,roundTime):
            # 保存上面到temp
            temp = []
            for j in range(0,matrixLen - i * 2 -1):
                temp.append(matrix[i][i + j])
            # 左边到上面
            for j in range(0,matrixLen - i * 2 - 1):
                matrix[i][i + j] = matrix[matrixLen - 1 - i - j][i]
            # 下面到左边
            for j in range(0, matrixLen - i * 2 - 1):
                matrix[matrixLen - 1 - i - j][i] = matrix[matrixLen - 1 - i][matrixLen - 1 - i - j]
            # 右边到下面
            for j in range(0, matrixLen - i * 2 - 1):
                matrix[matrixLen - 1 - i][matrixLen - 1 - i - j] = matrix[i + j][matrixLen - 1 - i]
            # temp到右边
            for j in range(0, matrixLen - i * 2 - 1):
                matrix[i + j][matrixLen - 1 - i] = temp[j]

s = Solution1()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(matrix)
print("---------------------------")
s.rotate(matrix)
print(matrix)
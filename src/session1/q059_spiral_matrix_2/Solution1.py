from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def generateMatrix(self, n):
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]
        # 初始化
        matrix = []
        for i in range(0,n):
            eachRow = []
            for j in range(0,n):
                eachRow.append(0)
            matrix.append(eachRow)
        round = n // 2
        num = 1
        for i in range(0,round):
            # 上边
            for j in range(0,n - 1 - 2 * i):
                matrix[i][i + j] = num
                num = num + 1
            # 右边
            for j in range(0,n - 1 - 2 * i):
                matrix[i + j][n - 1 - i] = num
                num = num + 1
            # 下边
            for j in range(0,n - 1 - 2 * i):
                matrix[n - 1 - i][n - 1 - i - j] = num
                num = num + 1
            # 左边
            for j in range(0,n - 1 - 2 * i):
                matrix[n - 1 - i - j][i] = num
                num = num + 1

        # 如果n为奇数，还需要在最中间放最后一个数字
        if n % 2 == 1:
            matrix[n // 2][ n // 2] = num
        return matrix

s = Solution1()
nArr = [2,3,4]
for i in range(0,len(nArr)):
    matrix = s.generateMatrix(nArr[i])
    PrintUtil.print_2d_num_array(matrix)


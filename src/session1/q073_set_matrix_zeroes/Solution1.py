from src.session1.common.PrintUtil import PrintUtil


class Solution1:
    def setZeroes(self, matrix):
        rowLen = len(matrix)
        if rowLen == 0:
            return
        columnLen = len(matrix[0])
        if columnLen == 0:
            return
        rowList = []
        columnList = []
        for i in range(0,rowLen):
            for j in range(0,columnLen):
                if matrix[i][j] == 0:
                    if rowList.count(i) == 0:
                        rowList.append(i)
                    if columnList.count(j) == 0:
                        columnList.append(j)
        for i in range(0,len(rowList)):
            matrix[rowList[i]] = [0 for i in range(0,columnLen)]
        for i in range(0,len(columnList)):
            columnIndex = columnList[i]
            for j in range(0,rowLen):
                matrix[j][columnIndex] = 0
        return

matrixArr = [[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
],[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]]
s = Solution1()
for i in range(0,len(matrixArr)):
    PrintUtil.print_2d_num_array(matrixArr[i])
    print("--------------")
    s.setZeroes(matrixArr[i])
    PrintUtil.print_2d_num_array(matrixArr[i])
    print("--------------")
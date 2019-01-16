class Solution1:
    def spiralOrder(self, matrix):
        rowLen = len(matrix)
        if rowLen == 0:
            return []
        columnLen = len(matrix[0])
        if columnLen == 0:
            return 0
        if rowLen < columnLen:
            minLen = rowLen
        else:
            minLen = columnLen
        round = minLen // 2
        ret = []
        for i in range(0,round):
            #上面
            for j in range(0,columnLen - 1 - i * 2):
                ret.append(matrix[i][i + j])
            #右面
            for j in range(0,rowLen - 1 - i * 2):
                ret.append(matrix[i + j][columnLen - 1 - i])
            #下面
            for j in range(0,columnLen - 1 - 2 * i):
                ret.append(matrix[rowLen - 1 - i][columnLen - 1 - j - i])
            #左面
            for j in range(0,rowLen - 1 - 2 * i):
                ret.append(matrix[rowLen - 1 - j - i][i])
        # 较短边为偶数，已经结束
        if minLen % 2 == 0:
            return ret
        else:
            # 行较短
            if rowLen < columnLen:
                for i in range(round,columnLen - round):
                    ret.append(matrix[rowLen // 2][i])
            # 列较短
            else:
                for i in range(round,rowLen - round):
                    ret.append(matrix[i][columnLen // 2])
            return ret

matrixArr = [[[1]],[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
],[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]]
s = Solution1()
for i in range(0,len(matrixArr)):
    print(s.spiralOrder(matrixArr[i]))
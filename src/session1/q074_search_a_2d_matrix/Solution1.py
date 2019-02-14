class Solution1:
    def searchMatrix(self, matrix, target):
        rowLen = len(matrix)
        if rowLen == 0:
            return False
        columnLen = len(matrix[0])
        if columnLen == 0:
            return False
        for i in range(0,rowLen):
            eachRow = matrix[i]
            if target <= eachRow[columnLen - 1] and target >= eachRow[0]:
                return self.seachInRow(eachRow, target)
        return False

    def seachInRow(self, oneRow, target):
        listLen = len(oneRow)
        left = 0
        right = listLen - 1
        while left < right:
            mid = (left + right) // 2
            if oneRow[mid] == target:
                return True
            elif oneRow[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return oneRow[left] == target

s = Solution1()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
targetArr = [3,13]
for i in range(0,len(targetArr)):
    print(s.searchMatrix(matrix,targetArr[i]))
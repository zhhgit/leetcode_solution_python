class Solution1:
    def __init__(self):
        self.haveFound = False

    def exist(self, board, word):
        rowLen = len(board)
        columnLen = len(board[0])
        for i in range(0, rowLen):
            for j in range(0, columnLen):
                if self.haveFound:
                    return self.haveFound
                else:
                    visited = [[False for i in range(0, columnLen)] for j in range(0, rowLen)]
                    self.backTracking(board, word, visited, i, j)
        return self.haveFound

    def backTracking(self, board, remain, visited, xPos, yPos):
        if not self.haveFound:
            if len(remain) == 0:
                self.haveFound = True
            elif len(remain) == 1 and remain[0] == board[xPos][yPos]:
                self.haveFound = True
            else:
                if remain[0] == board[xPos][yPos]:
                    newRemain = remain[1:len(remain)]
                    # 上
                    if self.possibleNext(xPos - 1, yPos, board) and not visited[xPos - 1][yPos]:
                        visited[xPos][yPos] = True
                        self.backTracking(board, newRemain, visited, xPos - 1, yPos)
                        visited[xPos][yPos] = False
                    # 下
                    if self.possibleNext(xPos + 1, yPos, board) and not visited[xPos + 1][yPos]:
                        visited[xPos][yPos] = True
                        self.backTracking(board, newRemain, visited, xPos + 1, yPos)
                        visited[xPos][yPos] = False
                    # 左
                    if self.possibleNext(xPos, yPos - 1, board) and not visited[xPos][yPos - 1]:
                        visited[xPos][yPos] = True
                        self.backTracking(board, newRemain, visited, xPos, yPos - 1)
                        visited[xPos][yPos] = False
                    # 右
                    if self.possibleNext(xPos, yPos + 1, board) and not visited[xPos][yPos + 1]:
                        visited[xPos][yPos] = True
                        self.backTracking(board, newRemain, visited, xPos, yPos + 1)
                        visited[xPos][yPos] = False

    def possibleNext(self,xPos,yPos,board):
        rowLen = len(board)
        columnLen = len(board[0])
        if xPos < 0 or xPos >= rowLen or yPos < 0 or yPos >= columnLen:
            return False
        else:
            return True

board = [
  ['A']
]
strArr = ["A"]
for i in range(0,len(strArr)):
    s = Solution1()
    print(s.exist(board,strArr[i]))
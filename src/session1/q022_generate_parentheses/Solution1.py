class Solution1:
    def __init__(self):
        self.list = []

    def generateParenthesis(self, n):
        if n == 0:
            return []
        tempList = []
        self.backTracking(tempList,0,0,n)
        return self.list

    def backTracking(self,tempList,leftNum,rightNum,n):
        """
        :param temp: 临时字符串
        :param leftNum:  左括号已经使用次数
        :param rightNum: 右括号已经使用次数
        :param n: n对
        :return: 空
        """
        if leftNum == n and rightNum == n and len(tempList) == 2 * n:
            str = self.getStrFromList(tempList)
            if self.list.count(str) == 0:
                self.list.append(str)
        else:
            if leftNum < n:
                tempList.append("(")
                self.backTracking(tempList,leftNum + 1,rightNum,n)
                if len(tempList) != 0:
                    tempList.pop()
            if leftNum > rightNum:
                tempList.append(")")
                self.backTracking(tempList,leftNum,rightNum + 1,n)
                if len(tempList) != 0:
                    tempList.pop()

    def getStrFromList(self,tempList):
        ret = ""
        for i in range(0,len(tempList)):
            ret = ret + tempList[i]
        return ret

n = 3
s = Solution1()
print(s.generateParenthesis(n))

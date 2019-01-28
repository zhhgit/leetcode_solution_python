class Solution1:
    def getPermutation(self, n, k):
        if n == 1 and k == 1:
            return "1"
        divisorArr = self.getDivisorArr(n)
        visited = self.getVisited(n)
        ret = ""
        for i in range(0,n - 1):
            divisor = divisorArr[n - 1 - i - 1]
            # 取第pos个未使用过的数字
            pos = (k - 1) // divisor + 1
            k = k - divisor * (pos - 1)
            ret = ret + self.getPosNumInVisited(visited,pos)
        ret = ret + self.getPosNumInVisited(visited,1)
        return ret

    def getDivisorArr(self,n):
        divisorArr = []
        temp = 1
        for i in range(1,n):
            temp = temp * i
            divisorArr.append(temp)
        return  divisorArr

    def getVisited(self,n):
        ret = []
        for i in range(0,n):
            ret.append(False)
        return ret

    def getPosNumInVisited(self,visited,pos):
        count = 0
        for i in range(0,len(visited)):
            if (not visited[i]):
                if pos == count + 1:
                    visited[i] = True
                    return str(i + 1)
                else:
                    count = count + 1

s = Solution1()
nArr = [3,4]
kArr = [3,9]
for i in range(0,len(nArr)):
    print(s.getPermutation(nArr[i],kArr[i]))
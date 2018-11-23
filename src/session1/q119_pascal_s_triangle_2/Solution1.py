class Solution1:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        curr = []
        for i in range(1,rowIndex + 1):
            prev = curr
            curr = []
            for j in range(0,i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j - 1] + prev[j])
        return curr

s = Solution1()
index = 4
print(s.getRow(index))

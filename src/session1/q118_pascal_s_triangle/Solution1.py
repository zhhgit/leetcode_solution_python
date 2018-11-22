class Solution1:
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        for i in range(1,numRows):
            prev = result[len(result) - 1]
            curr = []
            for j in range(0,i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j - 1] + prev[j])
            result.append(curr)
        return result

s = Solution1()
num = 5
print(s.generate(num))
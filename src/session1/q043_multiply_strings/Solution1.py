class Solution1:
    def multiply(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        arr = []
        for i in range(0,len1 + len2 - 1):
            temp = 0
            for j in range(0,i + 1):
                if len1 >= j + 1 and len2 >= i - j + 1:
                    charNum1 = int(num1[len1 - j - 1])
                    charNum2 = int(num2[len2 - (i - j) - 1])
                    temp = temp + charNum1 * charNum2
            arr.append(temp)
        return self.getResult(arr)

    def getResult(self,arr):
        increase = 0
        for i in range(0,len(arr)):
            tempSum = increase + arr[i]
            if tempSum >= 10:
                increase = tempSum // 10
                arr[i] = tempSum % 10
            else:
                increase = 0
                arr[i] = tempSum % 10
        if increase > 0:
            arr.append(increase)
        ret = ""
        for i in range(len(arr) - 1,-1,-1):
            ret = ret + str(arr[i])
        return str(int(ret))

s = Solution1()
num1 = "123"
num2 = "456"
print(s.multiply(num1,num2))
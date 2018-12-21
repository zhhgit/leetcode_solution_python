class Solution1:
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if (dividend > 0 and divisor > 0) or(dividend < 0 and divisor < 0):
            return self.calPositive(abs(dividend),abs(divisor))
        else:
            return -self.calPositive(abs(dividend), abs(divisor))


    def calPositive(self,dividend,divisor):
        """
        计算正整数情况
        :param dividend: 
        :param divisor: 
        :return: 
        """
        result = 0
        while dividend >= divisor:
            tempResult = divisor
            temp = 1
            while dividend >= (tempResult << 1):
                tempResult = tempResult << 1
                temp = temp << 1
            result = result + temp
            dividend = dividend - tempResult
        return result

s = Solution1()
dividendArr = [6,9,9,-10,10,2**31 - 1,-2**31]
divisorArr = [2,2,4,7,3,-1,-1]
for i in range(0,len(dividendArr)):
    print(str(dividendArr[i]) + "/" + str(divisorArr[i]) + "=" + str(s.divide(dividendArr[i],divisorArr[i])))
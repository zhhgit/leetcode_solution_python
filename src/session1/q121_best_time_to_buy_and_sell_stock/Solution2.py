class Solution1:
    def maxProfit(self, prices):
        pricesLen = len(prices)
        diffArr = []
        diffArr.append(0)
        for i in range(1,pricesLen):
            diffArr.append(prices[i] - prices[i - 1])
        tempSum = 0
        maxRet = 0
        for i in range(0,pricesLen):
            tempSum = tempSum + diffArr[i]
            if tempSum < 0:
                tempSum = 0
            else:
                maxRet = max(maxRet,tempSum)
        return maxRet

s = Solution1()
pricesArr = [[7,1,5,3,6,4],[7,6,4,3,1]]
for prices in pricesArr:
    print(s.maxProfit(prices))
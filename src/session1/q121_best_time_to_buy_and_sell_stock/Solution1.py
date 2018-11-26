class Solution1:
    def maxProfit(self, prices):
        maxRet = 0
        for i in range(1,len(prices)):
            temp = prices[i] - self.minBefore(prices,i)
            maxRet = max(maxRet,temp)
        return maxRet

    def minBefore(self, prices, pos):
        minRet = prices[0]
        for i in range(0,pos):
            minRet = min(minRet,prices[i])
        return minRet

s = Solution1()
pricesArr = [[7,1,5,3,6,4],[7,6,4,3,1]]
for prices in pricesArr:
    print(s.maxProfit(prices))

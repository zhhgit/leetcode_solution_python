class Solution1:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        diff = [0]
        for i in range(1,len(prices)):
            diff.append(prices[i] - prices[i - 1])
        maxRet = 0
        temp = 0
        for i in range(1,len(prices)):
            temp = temp + diff[i]
            if temp > 0:
                maxRet += temp
                temp = 0
            else:
                temp = 0
        return maxRet

s = Solution1()
arr = [[7,1,5,3,6,4],[1,2,3,4,5]]
for prices in arr:
    print(s.maxProfit(prices))
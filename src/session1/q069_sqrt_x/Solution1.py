class Solution1:
    def mySqrt(self, x):
        i = 0
        while i**2 <= x:
            i = i + 1
        return i - 1

s = Solution1()
xArr = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(xArr)):
    print(s.mySqrt(xArr[i]))
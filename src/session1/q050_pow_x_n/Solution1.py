class Solution1:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == -2**31:
            return x * self.myPowPostiveN(1/x, 2**31 - 1)
        if n < 0:
            return self.myPowPostiveN(1/x,-n)
        else:
            return self.myPowPostiveN(x,n)

    def myPowPostiveN(self,x,n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 1:
            return self.myPowPostiveN(x**2,n // 2) * x
        else:
            return self.myPowPostiveN(x**2,n // 2)

xArr = [2.0,2.1,2.0,2.0]
nArr = [10,3,-2,-2147483648]
s = Solution1()
for i in range(0,len(nArr)):
    print(s.myPow(xArr[i],nArr[i]))
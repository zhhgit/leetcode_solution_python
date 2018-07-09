class Solution1:
    def reverse(self, x):
        ret = 0
        if x < 0:
            ret =  0 - self.reversePositive(0 - x)
        elif x == 0:
            ret = 0
        else:
            ret = self.reversePositive(x)
        if 2**31 - 1 < ret  or ret < 0 - 2**31:
            return 0
        else:
            return ret

    def reversePositive(self,x):
        ret = 0
        while x > 0:
            ret = ret * 10 + x % 10
            x = x // 10
        return ret

s = Solution1()
arr = [122,-2,-321,120,1534236469]
for i in arr:
    print(s.reverse(i))
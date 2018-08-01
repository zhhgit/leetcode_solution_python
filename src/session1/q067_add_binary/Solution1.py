class Solution1:
    def addBinary(self, a, b):
        aLen = len(a)
        bLen = len(b)
        if aLen <= bLen:
            newA = self.extendStr(a,bLen - aLen)
            newB = b
        else:
            newA = a
            newB = self.extendStr(b,aLen - bLen)
        newLen = len(newA)
        increase = 0
        ret = ""
        for i in range(newLen - 1,-1,-1):
            num = int(newA[i]) + int(newB[i]) + increase
            if num >= 2:
                increase = num // 2
                ret = str(num % 2) + ret
            else:
                increase = 0
                ret = str(num) + ret
        if increase > 0:
            ret = str(increase) + ret
        return ret

    def extendStr(self,str,len):
        for i in range(0,len):
            str = "0" + str
        return str

s = Solution1()
s1 = "1010"
s2 = "1011"
print(s.addBinary(s1,s2))
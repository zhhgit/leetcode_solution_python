class Solution1:
    def intToRoman(self, num):
        retStr = ""
        pos = 0
        numStr = str(num)
        for i in range(0,len(numStr)):
            retStr = retStr + self.eachPos(int(numStr[i]),len(numStr) - 1 - i)
        return retStr

    def eachPos(self,eachNum,pos):
        retStr = ""
        if pos == 0:
            one = "I"
            half = "V"
            full = "X"
        elif pos == 1:
            one = "X"
            half = "L"
            full = "C"
        elif pos == 2:
            one = "C"
            half = "D"
            full = "M"
        else:
            one = "M"
        if eachNum <= 3:
            for i in range(0,eachNum):
                retStr = retStr + one
        elif eachNum == 4:
            retStr = one + half
        elif eachNum == 5:
            retStr = half
        elif eachNum >= 6 and eachNum <=8:
            retStr = half
            for i in range(0,eachNum - 5):
                retStr = retStr + one
        elif eachNum == 9:
            retStr = one + full
        return retStr

s = Solution1()
arr = [3,4,9,58,1994,6]
for i in range(0,len(arr)):
    print(s.intToRoman(arr[i]))
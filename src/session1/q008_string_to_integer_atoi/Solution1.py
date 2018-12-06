class Solution1:
    def myAtoi(self, str):
        strLen = len(str)
        i = 0
        # 跳过起始位置
        while i < strLen and str[i] == " ":
            i = i + 1
        if i == strLen:
            return 0
        if str[i] == "+":
            return self.convertPureNum("+",str[i + 1:strLen])
        elif str[i] == "-":
            return 0 - self.convertPureNum("-",str[i + 1:strLen])
        else:
            return self.convertPureNum("+",str[i:strLen])

    def convertPureNum(self,sign,str):
        ret = 0
        for i in range(0,len(str)):
            if not str[i].isdigit():
                return ret
            else:
                ret = ret * 10 + int(str[i])
                if sign == "+":
                    if (ret > 2**31 -1):
                        return 2**31 - 1
                elif sign == "-":
                    if (ret > 2**31):
                        return 2**31
        return ret

s = Solution1()
arr = ["   123","-21","+3","a12",str(2**31),str(2**31 - 1),str(-2**31),str(-2**31 - 1)]
for i in range(0,len(arr)):
    print(s.myAtoi(arr[i]))
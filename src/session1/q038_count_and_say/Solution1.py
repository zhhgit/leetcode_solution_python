class Solution1:
    def countAndSay(self, n):
        ret = []
        ret.append("1")
        for i in range(1,n):
            ret.append(self.countLast(ret[i-1]))
        return ret[n - 1]

    def countLast(self,last):
        ret = ""
        strLen = len(last)
        num = None
        count = 0
        for i in range(0,strLen):
            if num is None:
                num = last[i]
                count = 1
            elif last[i] != last[i-1]:
                ret = ret + str(count) + num
                num = last[i]
                count = 1
            else:
                count += 1
        ret = ret + str(count) + num
        return ret

s = Solution1()
arr = [1,2,3,4,5]
for i in arr:
    print(s.countAndSay(i))
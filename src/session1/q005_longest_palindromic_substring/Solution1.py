class Solution1:

    def __init__(self):
        self.retStr = ""

    def longestPalindrome(self, s):
        sLen = len(s)
        for pos in range(0,sLen):
            self.extend(s,pos,pos)
            self.extend(s,pos,pos + 1)
        return self.retStr

    # 向两侧扩展
    def extend(self,s,leftPos,rightPos):
        while self.validIndex(leftPos,s) and self.validIndex(rightPos,s):
            if s[leftPos] == s[rightPos]:
                str = s[leftPos:rightPos + 1]
                if len(str) > len(self.retStr):
                    self.retStr = str
                leftPos = leftPos - 1
                rightPos = rightPos + 1
            else:
                break

    # 合法位置
    def validIndex(self,pos,s):
        sLen = len(s)
        return pos >= 0 and pos <= sLen - 1

arr = ["babad","cbbd","caba"]
for str in arr:
    s = Solution1()
    print(s.longestPalindrome(str))
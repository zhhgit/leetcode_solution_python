class Solution1:
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        strLen = len(s)
        i = strLen - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        if i < 0:
            return 0
        endPos = i
        while i >= 0 and s[i] != " ":
            i -= 1
        startPos = i + 1
        return endPos - startPos + 1

s = Solution1()
arr = ["Hello World","","      "," dafd  ","dafda   "]
for i in range(0,len(arr)):
    print(s.lengthOfLastWord(arr[i]))

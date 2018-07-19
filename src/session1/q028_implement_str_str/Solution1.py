class Solution1:
    def strStr(self, haystack, needle):
        hLen = len(haystack)
        nLen = len(needle)
        if nLen == 0:
            return 0
        for i in range(0,hLen - nLen + 1):
            if self.fitAtPos(haystack,needle,i):
                return i
        return -1

    def fitAtPos(self,haystack,needle,pos):
        hLen = len(haystack)
        nLen = len(needle)
        for i in range(0,nLen):
            if needle[i] != haystack[pos + i]:
                return False
        return True

s = Solution1()
haystackArr = ["hello","aaaaa"]
needleArr = ["ll","bba"]
for i in range(0,len(haystackArr)):
    print(s.strStr(haystackArr[i],needleArr[i]))
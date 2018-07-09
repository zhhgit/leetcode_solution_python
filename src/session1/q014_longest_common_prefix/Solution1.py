class Solution1:
    def longestCommonPrefix(self, strs):
        size = len(strs)
        if size == 0:
            return ""
        minLen = self.shortest_len(strs)
        for i in range(0,minLen):
            if not self.all_same(strs,i):
                return strs[0][0:i]
        return strs[0][0:minLen]

    def all_same(self,strs,pos):
        strLen = len(strs)
        c = strs[0][pos]
        for i in range(0,strLen):
            if strs[i][pos] != c:
                return False
        return True

    def shortest_len(self,strs):
        ret = len(strs[0])
        for i in range(0,len(strs)):
            ret = min(ret,len(strs[i]))
        return ret

s = Solution1()
strs = ["flower","flow","flight","a"]
print(s.longestCommonPrefix(strs))
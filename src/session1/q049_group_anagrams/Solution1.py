class Solution1:
    def groupAnagrams(self, strs):
        dict = {}
        for i in range(0,len(strs)):
            feature = self.getFeature(strs[i])
            if feature in dict:
                targetList = dict[feature]
                targetList.append(strs[i])
            else:
                dict[feature] = []
                dict[feature].append(strs[i])
        ret = []
        for feature in dict:
            ret.append(dict[feature])
        return ret

    def getFeature(self,str):
        arr = []
        for i in range(0,len(str)):
            arr.append(str[i])
        arr.sort()
        return "".join(arr)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution1()
print(s.groupAnagrams(strs))

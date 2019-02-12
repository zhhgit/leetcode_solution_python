class Solution1:
    def simplifyPath(self, path):
        strArr = path.split("/",-1)
        tempList = []
        for i in range(0,len(strArr)):
            if strArr[i] != "":
                if strArr[i] == "..":
                    if len(tempList) > 0:
                        tempList.pop()
                elif strArr[i] == ".":
                    continue
                else:
                    tempList.append(strArr[i])
        return self.getStrFromList(tempList)

    def getStrFromList(self,tempList):
        if len(tempList) == 0:
            return "/"
        ret = ""
        for i in range(0,len(tempList)):
            ret += "/"
            ret += tempList[i]
        return ret

s = Solution1()
arr = ["/a/./b/../../c/","/../","/home/","/home//foo/","/.","/..."]
for item in range(0,len(arr)):
    print(s.simplifyPath(arr[item]))
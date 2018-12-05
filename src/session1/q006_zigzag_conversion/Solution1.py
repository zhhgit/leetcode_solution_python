class Solution1:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        lists = []
        for i in range(0,numRows):
            lists.append([])
        eachGroupNum = 2 * numRows - 2
        for i in range(0, len(s)):
            index = i % eachGroupNum
            if index < numRows:
                pos = index
            else:
                pos = 2 * numRows - 2 - index
            lists[pos].append(s[i])
        return self.readLists(lists)

    def readLists(self, lists):
        listSize = len(lists)
        ret = ""
        for i in range(0,listSize):
            str = "".join(lists[i])
            ret = ret + str
        return ret

s = Solution1()
arr = ["PAYPALISHIRING","abcdefg","abcd"]
numArr = [3,2,1]
for i in range(0,len(arr)):
    print(s.convert(arr[i],numArr[i]))
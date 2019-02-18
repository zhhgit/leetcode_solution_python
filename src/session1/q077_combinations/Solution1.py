import copy

class Solution1:
    def combine(self, n, k):
        lists = []
        tempList = []
        self.backTracking(n,k,lists,tempList,0)
        return lists

    def backTracking(self, n, k, lists, tempList, pos):
        if len(tempList) == k:
            addList = copy.deepcopy(tempList)
            if lists.count(addList) == 0:
                lists.append(addList)
        else:
            for i in range(pos, n):
                tempList.append(i + 1)
                self.backTracking(n,k,lists,tempList,i + 1)
                if len(tempList) > 0:
                    tempList.pop()

n = 4
k = 2
s = Solution1()
print(s.combine(n,k))


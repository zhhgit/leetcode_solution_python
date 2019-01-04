import copy

class Solution1:
    def combinationSum2(self, candidates, target):
        if len(candidates) == 0:
            return []
        candidates.sort()
        lists = []
        tempList = []
        self.backTracking(candidates,lists,tempList,0,target)
        return lists

    def backTracking(self,candidates,lists,tempList,startPos,remain):
        if remain == 0:
            addList = copy.deepcopy(tempList)
            if lists.count(addList) == 0:
                lists.append(addList)
        else:
            for i in range(startPos,len(candidates)):
                if remain >= candidates[i]:
                    tempList.append(candidates[i])
                    self.backTracking(candidates,lists,tempList,i + 1,remain - candidates[i])
                    if (len(tempList) > 0):
                        tempList.pop()

arr = [10,1,2,7,6,1,5]
target = 8
s = Solution1()
print(s.combinationSum2(arr,target))

import copy

class Solution1:
    def combinationSum(self, candidates, target):
        candidates.sort()
        lists = []
        tempList = []
        self.backTracking(lists,tempList,candidates,target,0)
        return lists

    def backTracking(self,lists,tempList,candidates,target,pos):
        if target == 0:
            if lists.count(tempList) == 0:
                addList = copy.deepcopy(tempList)
                lists.append(addList)
        else:
            for i in range(pos,len(candidates)):
                if (candidates[i] <= target):
                    tempList.append(candidates[i])
                    self.backTracking(lists,tempList,candidates,target - candidates[i],i)
                    if len(tempList) > 0:
                        tempList.pop()

s = Solution1()
candidatesArr = [[2,3,6,7],[2,3,5]]
targetArr = [7,8]
for i in range(0,len(targetArr)):
    print(s.combinationSum(candidatesArr[i],targetArr[i]))

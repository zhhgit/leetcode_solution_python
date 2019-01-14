import copy

class Solution1:
    def permuteUnique(self, nums):
        nums.sort()
        lists = []
        tempList = []
        visited = []
        for i in range(0,len(nums)):
            visited.append(False)
        self.backTracking(nums,lists,tempList,visited)
        return lists

    def backTracking(self,nums,lists,tempList,visited):
        numsLen = len(nums)
        if len(tempList) == numsLen:
            addList = copy.deepcopy(tempList)
            if lists.count(addList) == 0:
                lists.append(addList)
        else:
            for i in range(0,numsLen):
                if not visited[i]:
                    visited[i] = True
                    tempList.append(nums[i])
                    self.backTracking(nums, lists, tempList, visited)
                    visited[i] = False
                    if len(tempList) > 0:
                        tempList.pop()

arr = [1,1,2]
s = Solution1()
print(s.permuteUnique(arr))

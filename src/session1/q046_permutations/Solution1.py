import copy

class Solution1:
    def permute(self, nums):
        numsLen = len(nums)
        if numsLen == 0:
            return []
        lists = []
        tempList = []
        visited = []
        for i in range(0,numsLen):
            visited.append(False)
        self.backTracking(nums,lists,tempList,visited)
        return lists

    def backTracking(self, nums, lists, tempList,visited):
        if len(tempList) == len(nums):
            addList = copy.deepcopy(tempList)
            if lists.count(addList) == 0:
                lists.append(addList)
        else:
            for i in range(0,len(nums)):
                if not visited[i]:
                    tempList.append(nums[i])
                    visited[i] = True
                    self.backTracking(nums, lists, tempList, visited)
                    visited[i] = False
                    if len(tempList) > 0:
                        tempList.pop()

s = Solution1()
nums = [1,2,3,4]
print(s.permute(nums))
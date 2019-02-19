import copy

class Solution1:
    def subsets(self, nums):
        lists = []
        tempList = []
        self.backTracking(nums,lists,tempList,0)
        return lists

    def backTracking(self,nums,lists,tempList,pos):
        addList = copy.deepcopy(tempList)
        lists.append(addList)
        for i in range(pos,len(nums)):
            tempList.append(nums[i])
            self.backTracking(nums,lists,tempList,i + 1)
            if len(tempList) > 0:
                tempList.pop()

nums = [1,2,3]
s = Solution1()
print(s.subsets(nums))

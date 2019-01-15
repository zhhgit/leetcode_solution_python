class Solution1:
    def fourSum(self, nums, target):
        numsLen = len(nums)
        if numsLen < 4:
            return []
        nums.sort()
        lists = []
        for i in range(0,numsLen - 3):
            for j in range(i + 1,numsLen - 2):
                self.findWithRemain(nums,lists,target,i,j)
        return lists

    def findWithRemain(self,nums,lists,target,i,j):
        numsLen = len(nums)
        remain = target - nums[i] - nums[j]
        left = j + 1
        right = numsLen - 1
        while left < right:
            if nums[left] + nums[right] == remain:
                addList = [nums[i],nums[j],nums[left],nums[right]]
                if lists.count(addList) == 0:
                    lists.append(addList)
                left = left + 1
                right = right - 1
            elif nums[left] + nums[right] < remain:
                left = left + 1
            else:
                right = right - 1

arr = [1, 0, -1, 0, -2, 2]
target = 0
s = Solution1()
print(s.fourSum(arr,target))

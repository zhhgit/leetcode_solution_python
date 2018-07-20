class Solution1:
    def searchInsert(self, nums, target):
        numsLen = len(nums)
        i = 0
        while i < numsLen:
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i += 1
            else:
                return i
        if i == numsLen:
            return numsLen

s = Solution1()
nums = [1,3,5,6]
targetArr = [5,2,7,0]
for i in targetArr:
    print(s.searchInsert(nums,i))
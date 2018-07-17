class Solution1:
    def removeDuplicates(self, nums):
        numLen = len(nums)
        index = 0
        for i in range(0,numLen):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index

s = Solution1()
lists = [[0,0,1,1,1,2,2,3,3,4],[1,1,2]]
for i in range(0,len(lists)):
    list = lists[i]
    print(s.removeDuplicates(list))
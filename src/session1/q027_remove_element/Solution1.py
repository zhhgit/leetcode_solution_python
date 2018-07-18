class Solution1:
    def removeElement(self, nums, val):
        index = 0
        for i in range(0,len(nums)):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

s = Solution1()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums,val))

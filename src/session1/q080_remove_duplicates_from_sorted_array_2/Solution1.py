class Solution1:
    def removeDuplicates(self, nums):
        numsLen = len(nums)
        index = 0
        dict = {}
        for i in range(0,numsLen):
            # 新出现的
            if i == 0 or nums[i] != nums[i - 1]:
                dict[nums[i]] = 1
                nums[index] = nums[i]
                index += 1
            else:
                alreadyTime = dict[nums[i]]
                if alreadyTime == 1:
                    dict[nums[i]] = 2
                    nums[index] = nums[i]
                    index += 1
        return index

s = Solution1()
nums = [1,1,1,2,2,3]
print(s.removeDuplicates(nums))

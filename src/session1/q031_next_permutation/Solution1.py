class Solution1:
    def nextPermutation(self, nums):
        numsLen = len(nums)
        if numsLen == 1:
            return
        i = numsLen - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i = i - 1
        # 全部递减，已经是最大，所以返回重排的最小
        if i == 0:
            return nums.sort()
        else:
            # 将i - 1位置与之后的比i - 1位置的值大的最小的数字交换
            minPos = self.findMinPosBehind(nums,i - 1)
            temp = nums[i - 1]
            nums[i - 1] = nums[minPos]
            nums[minPos] = temp
            # 再将i - 1位置之后的值重新升序排列
            self.sortPartNums(nums,i - 1)

    def findMinPosBehind(self,nums,pos):
        target = nums[pos]
        tempMin = nums[pos + 1]
        tempPos = pos + 1
        for i in range(pos + 1,len(nums)):
            if nums[i] > target and nums[i] < tempMin:
                tempMin = nums[i]
                tempPos = i
        return tempPos

    def sortPartNums(self,nums,pos):
        part = nums[pos + 1:len(nums)]
        part.sort()
        for i in range(0,len(part)):
            nums[pos + 1 + i] = part[i]

s = Solution1()
numsArr = [[1,2,3],[3,2,1],[1,1,5],[2,3,1]]
for i in range(0,len(numsArr)):
    s.nextPermutation(numsArr[i])
    print(numsArr[i])
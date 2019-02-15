from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def sortColors(self, nums):
        numsLen = len(nums)
        zeroPos = 0
        twoPos = numsLen - 1
        for i in range(0, numsLen):
            while nums[i] == 2 and i < twoPos:
                self.swap(nums, i, twoPos)
                twoPos -= 1
            while nums[i] == 0 and i > zeroPos:
                self.swap(nums, i, zeroPos)
                zeroPos += 1

    def swap(self,nums,posA,posB):
        temp = nums[posA]
        nums[posA] = nums[posB]
        nums[posB] = temp

numsArr = [[2,0,2,1,1,0],[2,0,2,1,0,1,0,0,0,2,1,0,1]]
s = Solution1()
for i in range(0,len(numsArr)):
    s.sortColors(numsArr[i])
    PrintUtil.print_num_array(numsArr[i])
    print()
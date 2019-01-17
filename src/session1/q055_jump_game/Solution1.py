class Solution1:
    def canJump(self, nums):
        numsLen = len(nums)
        if numsLen == 1:
            return True
        farrest = 0
        pos = 0
        while pos <= farrest:
            temp = nums[pos] + pos
            if temp >= numsLen - 1:
                return True
            farrest = max(farrest,temp)
            pos = pos + 1
        return False

s = Solution1()
numsArr = [[2,3,1,1,4],[3,2,1,0,4],[2,0,0]]
for i in range(0,len(numsArr)):
    print(s.canJump(numsArr[i]))
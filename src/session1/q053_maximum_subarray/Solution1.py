class Solution1:
    def maxSubArray(self, nums):
        numsLen = len(nums)
        ret = []
        maxVal = nums[0]
        for i in range(0,numsLen):
            if i == 0:
                ret.append(nums[i])
            else:
                if (ret[i - 1] > 0):
                    ret.append(ret[i - 1] + nums[i])
                else:
                    ret.append(nums[i])
            maxVal = max(maxVal,ret[i])
        return maxVal

s = Solution1()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(arr))

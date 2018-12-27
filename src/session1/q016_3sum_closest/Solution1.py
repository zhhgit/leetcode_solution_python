class Solution1:
    def threeSumClosest(self, nums, target):
        nums.sort()
        numsLen = len(nums)
        minDiff = 2**31 - 1
        ret = None
        for i in range(0,numsLen - 2):
            remain = target - nums[i]
            left = i + 1
            right = numsLen - 1
            while left < right:
                tempSum = nums[left] + nums[right]
                diff = abs(tempSum - remain)
                if diff < minDiff:
                    ret = tempSum + nums[i]
                    minDiff = diff
                if tempSum < remain:
                    left = left + 1
                elif tempSum > remain:
                    right = right - 1
                else:
                    return target
        return ret

s = Solution1()
arr = [1,1,1,0]
targetArr = [-100]
for i in range(0,len(targetArr)):
    print(s.threeSumClosest(arr,targetArr[i]))
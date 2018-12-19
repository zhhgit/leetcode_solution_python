class Solution1:
    def searchRange(self, nums, target):
        numsLen = len(nums)
        if numsLen == 0:
            return [-1,-1]
        left = 0
        right = numsLen - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return self.extendAtPos(nums,mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return self.extendAtPos(nums,left)
        else:
            return [-1,-1]

    def extendAtPos(self,nums,pos):
        ret = []
        target = nums[pos]
        left = pos
        while left >= 0 and nums[left] == target:
            left = left - 1
        ret.append(left + 1)
        right = pos
        while right < len(nums) and nums[right] == target:
            right = right + 1
        ret.append(right - 1)
        return ret

s = Solution1()
nums = [1]
targetArr = [1]
for i in range(0,len(targetArr)):
    print(s.searchRange(nums,targetArr[i]))


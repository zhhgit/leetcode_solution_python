class Solution1:
    def search(self, nums, target):
        numsLen = len(nums)
        if numsLen == 0:
            return False
        left = 0
        right = numsLen - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 转轴在右，左侧单调增
            elif nums[mid] > nums[right]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 转轴在左，右侧单调增
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right = right - 1
        if nums[left] == target:
            return True
        else:
            return False

s = Solution1()
nums = [1,3,5]
targetArr = [1]
for i in range(0,len(targetArr)):
    print(s.search(nums,targetArr[i]))
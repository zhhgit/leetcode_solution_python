class Solution1:
    def search(self, nums, target):
        numsLen = len(nums)
        if numsLen == 0:
            return -1
        left = 0
        right = numsLen - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左侧单调增，转轴在右侧
            elif nums[mid] > nums[right]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右侧单调增，转轴在左侧
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[left] == target:
            return left
        else:
            return  -1

s = Solution1()
nums = [3,1]
targetArr = [0]
for i in range(0,len(targetArr)):
    print(s.search(nums,targetArr[i]))
class Solution1:

    def __init__(self):
        self.ret = []

    def threeSum(self, nums):
        nums.sort()
        numsLen = len(nums)
        for i in range(0,numsLen - 2):
            # 跳过重复
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSumWithRemain(nums,i)
        return self.ret

    def twoSumWithRemain(self,nums,pos):
        numsLen = len(nums)
        remain = 0 - nums[pos]
        # 如果remain为负数，直接跳过
        if remain >= 0:
            left = pos + 1
            right = numsLen - 1
            while left < right:
                if nums[left] + nums[right] == remain:
                    addArr = [nums[pos], nums[left], nums[right]]
                    self.ret.append(addArr)
                    # 跳过重复
                    while left + 1 < numsLen and nums[left + 1] == nums[left]:
                        left = left + 1
                    left = left + 1
                    while right - 1 >= 0 and nums[right - 1] == nums[right]:
                        right = right - 1
                    right = right - 1
                elif nums[left] + nums[right] < remain:
                    left = left + 1
                elif nums[left] + nums[right] > remain:
                    right = right - 1

arr = [-1, 0, 1, 2, -1, -4]
s = Solution1()
print(s.threeSum(arr))
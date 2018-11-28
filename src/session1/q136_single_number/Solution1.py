class Solution1:
    def singleNumber(self, nums):
        nums.sort()
        pairs = len(nums) // 2
        for i in range(0,pairs):
            if nums[i * 2] != nums[i * 2 + 1]:
                return nums[i * 2]
        return nums[len(nums) - 1]

s = Solution1()
arr = [[2,2,1],[4,2,1,2,1],[2,1,1,3,3]]
for item in arr:
    print(s.singleNumber(item))
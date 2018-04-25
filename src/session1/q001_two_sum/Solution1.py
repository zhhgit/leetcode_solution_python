class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mapObj = {}
        ret = [0,0]
        for i in range(0,len(nums)):
            num = nums[i]
            remain = target - num
            if remain in mapObj:
                ret[0] = mapObj[remain]
                ret[1] = i
                return ret
            else:
                mapObj[num] = i
        return ret

s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums,target))
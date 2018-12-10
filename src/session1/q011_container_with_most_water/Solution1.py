class Solution:
    def maxArea(self, height):
        arrLen = len(height)
        ret = min(height[0],height[arrLen - 1]) * (arrLen - 1)
        left = 0
        right = arrLen - 1
        while left < right:
            if (height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
            newArea = min(height[left],height[right]) * (right - left)
            ret = max(ret,newArea)
        return ret

arr = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(arr))
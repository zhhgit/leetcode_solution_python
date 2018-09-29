class Solution2:
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            # mid过大
            if x // mid < mid:
                right = mid - 1
            # mid过小或正好符合
            else:
                # 检测一下mid + 1是否仍然太小，此情况是mid过小或者正好，mid + 1又过大，所以mid正好
                if x // (mid + 1) < (mid + 1):
                    return mid
                # mid仍然太小
                else:
                    left = mid + 1
        return left

s = Solution2()
xArr = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(xArr)):
    print(s.mySqrt(xArr[i]))
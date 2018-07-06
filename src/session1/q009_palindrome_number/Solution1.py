class Solution1:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            old = x
            target = 0
            while old > 0:
                target = target * 10 + old % 10
                old = old // 10
            return target == x

s = Solution1()
arr = [121,-121,1,22,345,10]
for i in range(0,len(arr)):
    print(s.isPalindrome(arr[i]))
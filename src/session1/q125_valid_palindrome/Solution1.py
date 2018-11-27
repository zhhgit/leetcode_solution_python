class Solution1:
    def isPalindrome(self, s):
        s = s.lower().strip()
        sLen = len(s)
        if sLen == 0:
            return True
        left = 0
        right = sLen - 1
        while left < right:
            while left < right and not self.isalphanumeric(s[left]):
                left = left + 1
            while left  < right and not self.isalphanumeric(s[right]):
                right = right - 1
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True

    # 是否字符或数字
    def isalphanumeric(self,str):
        return str.isalpha() or str.isdigit()

s = Solution1()
arr = ["A man, a plan, a canal: Panama","race a car","   aba","9P"]
for str in arr:
    print(s.isPalindrome(str))
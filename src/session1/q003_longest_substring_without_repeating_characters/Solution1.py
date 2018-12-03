class Solution1:
    def lengthOfLongestSubstring(self, s):
        sLen = len(s)
        if sLen <= 1:
            return sLen
        maxRet = 1
        left = 0
        right = 0
        dict = {}
        dict[s[0]] = 1
        for i in range(1,sLen):
            curr = s[i]
            if curr not in dict:
                dict[curr] = 1
                right = i
            else:
                while s[left] != curr:
                    dict.pop(s[left])
                    left = left + 1
                left = left + 1
            maxRet = max(maxRet,right - left + 1)
        return maxRet

arr = ["abcabcbb","bbbbb","pwwkew"]
s = Solution1()
for i in range(0,len(arr)):
    print(s.lengthOfLongestSubstring(arr[i]))

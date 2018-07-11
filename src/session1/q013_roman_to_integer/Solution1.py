class Solution1:
    def romanToInt(self, s):
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum1 = 0
        for c in s:
            sum1 += dict[c]
        sum2 = 0
        for i in range(0,len(s) - 1):
            if dict[s[i]] < dict[s[i + 1]]:
                sum2 += dict[s[i]]
        return sum1 - 2 * sum2

s = Solution1()
arr = ["III","IV","IX","LVIII","MCMXCIV",""]
for item in arr:
    print(s.romanToInt(item))
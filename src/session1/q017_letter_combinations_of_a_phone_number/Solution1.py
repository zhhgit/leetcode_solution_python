class Solution1:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        prev = []
        curr = []
        for i in range(0,len(digits)):
            digit = digits[i]
            possibleChar = self.str2Arr(dict[digit])
            curr = []
            if len(prev) == 0:
                for j in range(0,len(possibleChar)):
                    curr.append(possibleChar[j])
            else:
                for j in range(0,len(prev)):
                    old = prev[j]
                    for k in range(0,len(possibleChar)):
                        curr.append(old + possibleChar[k])
            prev = curr
        return curr

    def str2Arr(self,s):
        sLen = len(s)
        ret = []
        for i in range(0,sLen):
            ret.append(s[i])
        return ret

digits = "23"
s = Solution1()
print(s.letterCombinations(digits))
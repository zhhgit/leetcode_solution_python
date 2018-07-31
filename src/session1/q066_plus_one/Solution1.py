from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def plusOne(self, digits):
        arrLen = len(digits)
        ret = []
        increase = 1
        for i in range(arrLen - 1,-1,-1):
            num = digits[i] + increase
            if num >= 10:
                ret.append(num % 10)
                increase = 1
            else:
                ret.append(num)
                increase = 0
        if increase == 1:
            ret.append(increase)
        ret.reverse()
        return ret

s = Solution1()
digitsArr = [[4,3,2,1],[1,1,9],[9]]
for i in range(0,len(digitsArr)):
    ret = s.plusOne(digitsArr[i])
    PrintUtil.print_num_array(ret)
    print()
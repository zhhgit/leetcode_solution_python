class Solution1:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [1,2]
        for i in range(2,n):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[len(steps) - 1]

s = Solution1()
arr = [1,2,3,4,5]
for i in arr:
    print(s.climbStairs(i))
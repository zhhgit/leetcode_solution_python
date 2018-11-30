class Solution1:
    def __init__(self):
        self.dict = {}
        self.eleList = []

    def push(self, x):
        self.eleList.append(x)
        size = len(self.eleList)
        if len(self.dict.keys()) == 0:
            self.dict[1] = x
        else:
            self.dict[size] = min(x,self.dict[size - 1])

    def pop(self):
        size = len(self.eleList)
        self.dict.pop(size)
        return self.eleList.pop(-1)

    def top(self):
        return self.eleList[len(self.eleList) - 1]

    def getMin(self):
        return self.dict[len(self.eleList)]

s = Solution1()
s.push(3)
s.push(2)
print(s.top())
print(s.getMin())
print(s.pop())
print(s.top())
print(s.getMin())
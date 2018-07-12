class Solution1:
    def isValid(self, s):
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == "(" or c == "[" or c == "{":
                    stack.append(c)
                elif (c == ")" and stack[len(stack) - 1] == "(") or (c == "]" and stack[len(stack) - 1] == "[") or (
                        c == "}" and stack[len(stack) - 1] == "{"):
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0

s = Solution1()
arr = ["()","()[]{}","(]","([)]","{[]}","","]"]
for item in arr:
    print(s.isValid(item))
